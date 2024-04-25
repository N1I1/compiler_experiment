import string

from my_token import Token
import initial

_LETTERS = set(string.ascii_letters)
_DIGITS = set(string.digits)
_WHITESPACE = set(" \t\n\r")
_RELATIONAL_OPERATORS = set("<>=")
_OPERATORS = set("+-*/")
_DELIMITERS = set(",;()[]")


_IDENTIFIER_STARTS = _LETTERS | set('_')
_IDENTIFIER_INNERS = _IDENTIFIER_STARTS | _DIGITS
_NUMERAL_STARTS = set(string.digits) # | set('+-.')

# 初始化 表格
KEYWORDS_TABLE = initial.initial_keywords()
identifiers_table = initial.initial_identifiers()
DELIMITERS_TABLE = initial.initial_delimiters()
OPERATORS_TABLE = initial.initial_operators()
RELATIONAL_TABLE = initial.initial_relational_operators()
constants_table = initial.initial_constant()


note_flag = False
def read_note_decorator(func):
    def wrapper(line, col):
        global note_flag
        if note_flag:
            while col < len(line):
                c = line[col]
                n = col + 1
                if c == '*' and n < len(line) and line[n] == '/':
                    note_flag = False
                    col += 2
                    break
                col += 1
            if not note_flag and col < len(line):
                return func(line, col)
            return None, 0
        else:
            return func(line, col)
    
    return wrapper


def is_valid_identifier(text):
    length = len(text)
    if text[0] not in _IDENTIFIER_STARTS:
        return False

    for i in range(length-1):
        if text[i+1] not in _IDENTIFIER_INNERS:
            return False
    return True

def is_constant(text):
    length = len(text)
    if text[0] == '-':
        if text[1] not in _DIGITS:
            return False
    elif text[0] not in _NUMERAL_STARTS:
        return False

    point_flag = False
    for i in range(length-1):
        if text[i+1] == '.':
            # 应不应该把 "1." ".1" "+1" "-1" "-.1" "+.1" 设置为错误????
            if point_flag:
                return False
            else:
                point_flag = True
        elif text[i+1] not in _DIGITS:
            return False
    return True


def tokenize_line(line, row):
    result = []
    text, col = next_candidate_token(line, 0)
    while text is not None:
        if text in KEYWORDS_TABLE:
            new_token = Token(row+1, col, text, 1)
        elif text in DELIMITERS_TABLE:
            new_token = Token(row+1, col, text, 2)
        elif text in OPERATORS_TABLE:
            new_token = Token(row+1, col, text, 3)
        elif text in RELATIONAL_TABLE:
            new_token = Token(row+1, col, text, 4)
        elif is_valid_identifier(text):
            if text not in identifiers_table:
                identifiers_table.append(len(identifiers_table), text)
            new_token = Token(row+1, col, text, 6)
        elif is_constant(text):
            if text not in constants_table:
                constants_table.append(len(constants_table), text)
            new_token = Token(row+1, col, text, 5)
        else:
            new_token = Token(row+1, col, text, 5)
            new_token.error()
        result.append(new_token)
        text, col = next_candidate_token(line, col+len(text)-1)
    
    # print('done')
    return result

@read_note_decorator
def next_candidate_token(line, col):

    def inner(c, sets):
        text = c
        j = col + 1
        while j < len(line):
            c = line[j]
            if c in sets:
                text += c
                j = j + 1
            else:
                return text, col+1
    
    def split_operator_and_note_symbol(c, sets):
        text = ''
        tmp = c
        j = col + 1
        flag = True
        while j < len(line):
            c = line[j]
            if c not in sets:
                if c in _DIGITS and tmp[-1] in _NUMERAL_STARTS:
                    text = tmp[:len(tmp)-1]
                else:
                    text = tmp
                break

            if flag:
                if c == '*':
                    text = tmp[:len(tmp)-1]
                    break
                elif c != '/':
                    flag = False
            else:
                if c == '/':
                    flag = True
            tmp += c
    
            j += 1
        if j == len(line):
            text = tmp
        
        return text, col + 1

    while col < len(line):
        c = line[col]
        if c in _WHITESPACE:
            col += 1
        elif c == '/':
            if col+1 < len(line) and line[col+1] == '*':
                global note_flag
                note_flag = True
                return None, 0

            else:
                return split_operator_and_note_symbol(c, _OPERATORS)

            # 考虑 /* 注释符就很臃肿这个地方
        elif c in _DELIMITERS:
            return c, col+1
        elif c in _RELATIONAL_OPERATORS:
            return inner(c, _RELATIONAL_OPERATORS)
        elif c in _OPERATORS:
            return inner(c, _OPERATORS)
        elif c in _IDENTIFIER_STARTS:
            return inner(c, _IDENTIFIER_INNERS)
        elif c in _NUMERAL_STARTS:
            # 实际上此处不会读取到负数，"-" 已经在上边被读取了，起初是为考虑添加负数，
            # 但是个人认为将负号分离，在之后的步骤(其他分析阶段)处理更好，
            # 只是将考虑负号的代码保留了
            text = c
            j = col + 1
            while j < len(line) and \
                line[j] not in _WHITESPACE|\
                        _DELIMITERS|\
                        _RELATIONAL_OPERATORS|\
                        _OPERATORS:
                text += line[j]
                j += 1
            return text, col+1
        else:
            return c, col+1
    # print('line done')
    return None, 0 