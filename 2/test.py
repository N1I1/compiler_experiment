from initial import *
from production import *
from mproduction import *
from grammar import *
from ll1 import create_ll1_table

initial_terminals('i+-*/()')
initial_non_terminals('EGTSF')
initial_start('E')


def main():
    E1 = Production('E', 'TG')
    G1 = Production('G', '+TG')
    G2 = Production('G', '-TG')
    G3 = Production('G', '@')
    T1 = Production('T', 'FS')
    S1 = Production('S', '*FS')
    S2 = Production('S', '/FS')
    S3 = Production('S', '@')
    F1 = Production('F', '(E)')
    F2 = Production('F', 'i')

    E = MProduction([E1])
    G = MProduction([G1, G2, G3])
    T = MProduction([T1])
    S = MProduction([S1, S2, S3])
    F = MProduction([F1, F2])
    print(E, G, T, S, F, sep='\n')
    print('--------')
    grammar = Grammar([E, G, T, S, F])

    # 建表

    table = create_ll1_table(grammar=grammar)
    print(table['G'][')'])

    # 按照表格 进行分析
    
main()
