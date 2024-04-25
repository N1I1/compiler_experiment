from grammar import Grammar
from initial import _EPSILON, _EOF, _TERMINALS, _NON_TERMINALS

# step1: input the principle
# step2: analyze the principle 
        # if wrong: error()
# step3: input the tokens stream
# step4: reduce according to the principle
# step5: done

def create_ll1_table(grammar: Grammar):
    first_sets = grammar.get_first_sets()
    follow_sets = grammar.get_follow_sets()
    productions = grammar.get_productions()
    table = {}

    for production in productions:
        cur_non_terminal = production.get_left()
        row_table = {}
        first_set = first_sets[cur_non_terminal]
        for terminal in first_set:
            if terminal == _EPSILON:
                continue
            row_table[terminal] = production.get_right()
        if _EPSILON in first_set:
            follow_set = follow_sets[cur_non_terminal]
            for terminal in follow_set:
                if terminal == _EPSILON:
                    continue
                row_table[terminal] = production.get_right()

        table[cur_non_terminal] = row_table
    return table    

def parser(table, input, start):
    input = input + _EOF
    stack = [_EOF, start]
    i = 0

    while i < len(input):
        print_stack(stack)
        print(input[i:])
        s = input[i]
        top = stack[-1]
        if  top == _EOF:
            print('success')
        elif top in _TERMINALS:
            stack.pop()
            i = i+1
        else:
            try:
                production = table[top][s]
                out = production.get_right()
                out.reverse()
                stack.extend(out)
            except KeyError:
                print('Error')

def print_stack(stack):
    for s in stack:
        print(s, end='')