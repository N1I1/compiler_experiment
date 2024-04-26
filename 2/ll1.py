from grammar import Grammar
from initial import _EPSILON, _EOF, _TERMINALS, _NON_TERMINALS

# step1: input the principle
# step2: analyze the principle 
# step3: input
# step4: parse according to the principle

def first(input: list, grammar: Grammar) -> set:
    if len(input) == 0:
        raise ValueError(f"input is None")
    if input[0] in _TERMINALS:
        return set(input[0])
    elif input[0] == _EPSILON:
        return set(_EPSILON)
    else:
        first_sets = grammar.get_first_sets()
        return first_sets[input[0]]

# 实际上用不到
def follow(input: list, grammar: Grammar) -> set:
    if len(input) == 0:
        raise ValueError(f"input is None")
    if input[0] in _TERMINALS:
        return set(_EPSILON)
    elif input[0] == _EPSILON:
        return set(_EPSILON)
    else:
        follow_sets = grammar.get_follow_sets()
        return follow_sets[input[-1]]

def create_ll1_table(grammar: Grammar):
    productions = grammar.get_productions()
    follow_sets = grammar.get_follow_sets()
    table = {}

    for production in productions:
        cur_non_terminal = production.get_left()
        row_table = {}
        for i, right_part in enumerate(production.get_right()):
            first_set = first(right_part, grammar)
            follow_set = follow_sets[cur_non_terminal]

            # print(first_set)
            for terminal in first_set:
                if terminal == _EPSILON:
                    continue
                row_table[terminal] = production[i]
            if _EPSILON in first_set:
                for terminal in follow_set:
                    row_table[terminal] = production[i]
        table[cur_non_terminal] = row_table
    return table    

def parser(table, input, start):
    input = input
    stack = [_EOF, start]
    procedure_count = 0
    i = 0
    print("{:<5}".format("步骤"), "{:<26}".format("分析栈"), \
          "{:<24}".format("剩余输入串"),"{:<24}".format("所用产生式"), "{:<30}".format("动作"))

    while i < len(input):
        print("{:<8}".format(procedure_count), end='')
        print("{:<30}".format(print_stack(stack)), end='')
        print("{:<30}".format(input[i:]), end='')
        s = input[i]
        top = stack[-1]
        if top == _EOF:
            print('\n')
            print('*' * 90)
            print('success')
            break
        elif top in _TERMINALS:
            stack.pop()
            print("{:<30}".format(''), end='')
            if procedure_count == 0:
                print("{:<30}".format('初始化'), end='')
            else:
                print("{:<30}".format('GETNEXT(I)'))
            i = i+1
        else:
            try:
                production = table[top][s]
                production_str = str(production)
                print("{:<30}".format(production_str), end='')
                stack.pop()
                print("POP", end='')
                right = production.get_right()
                out = right.copy()
                out.reverse()
                if _EPSILON not in out:
                    stack.extend(out)
                    print(f", PUSH{right}", end='')
                print()
            except KeyError:
                print('Error')
        procedure_count += 1


def print_stack(stack):
    res = ''
    for s in stack:
        res += s
    return res
