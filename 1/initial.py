from table import Table

def initial_keywords(keys=[i for i in range(8)], 
                     items = [
                         'do',
                         'end',
                         'for',
                         'if',
                         'printf',
                         'scanf',
                         'then',
                         'while',
                         ] ):
    
    return Table('关键字表', keys, items)

def initial_identifiers(keys=[], items=[]):
    return Table('标识符标识符表',keys, items)
    
def initial_delimiters(keys=[i for i in range(6)],
                        items = [
                            ',',
                            ';',
                            '(',
                            ')',
                            '[',
                            ']',
                            ] ):
    return Table('分界符表', keys, items)

def initial_operators(keys=[
                        '10H',
                        '11H',
                        '20H',
                        '21H',
                        ], 
                    items=[
                        '+',
                        '-',
                        '*',
                        '/',
                        ]):
    return Table('算数运算符表', keys, items)

def initial_relational_operators(
        keys=[
            '00H',
            '01H',
            '02H',
            '03H',
            '04H',
            '05H',
            ],
        items=[
            '<',
            '<=',
            '=',
            '>',
            '>=',
            '<>',
            ]):
    return Table('关系运算符表', keys, items)

def initial_constant(keys=[], items=[]):
    return Table('常数表', keys, items)