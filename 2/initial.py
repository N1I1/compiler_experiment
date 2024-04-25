_START_SYMBOLS = set()
_TERMINALS = set()
_NON_TERMINALS = set()
_EPSILON = '@'
_EOF = '$'


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
