_START_SYMBOLS = set()
_TERMINALS = set()
_NON_TERMINALS = set()
_EPSILON = '@'
_EOF = '$'

def initial_from_file(filename: str) -> list:
    with open(filename, 'r') as f:
        terminals = f.readline()
        terminals = terminals[:-1]
        non_terminals = f.readline()
        non_terminals = non_terminals[:-1]
        start_symbols = f.readline()
        start_symbols = start_symbols[:-1]
        lines = f.readlines()
        
        # print(terminals)
        # print(non_terminals)
        initial_terminals(terminals)
        initial_non_terminals(non_terminals)
        initial_start(start_symbols)

        return lines




# 简单地读取终结符、非终结符

def initial_terminals(candidate_terminals):
    for terminal in candidate_terminals:
        _TERMINALS.add(terminal)

def initial_start(candidate_start_symbols):
    for candidate_start_symbol in candidate_start_symbols:
        if candidate_start_symbol not in _NON_TERMINALS:
            raise ValueError(f"{candidate_start_symbol} is not a non_terminal")
        _START_SYMBOLS.add(candidate_start_symbol)

def initial_non_terminals(candidate_non_terminals):
    for non_terminals in candidate_non_terminals:
        _NON_TERMINALS.add(non_terminals)

def set_epsilon(char):
    if len(char) > 1:
        raise ValueError(f"EPSILON should be a single character")
    _EPSILON = char

def set_eof(char):
    if len(char) > 1:
        raise ValueError(f"EOF should be a single character")
    _EOF = char