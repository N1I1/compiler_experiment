from augmented_grammar import AugmentedGrammar
from ..e2.grammar import first
from item_1 import Item_1
from ..e2.initial import _EOF, _EPSILON, _NON_TERMINALS
from state import State

class LR1Parser:
    def __init__(self, grammar: AugmentedGrammar):
        self.grammar = grammar
        self.productions_dict = self.grammar.get_productions_dict()
    
    def generate_item_1s(self):
        raise NotImplemented
        start_production = self.grammar.get_start_production()
        productions = self.grammar.get_productions()

        start_item_1 = Item_1(start_production, 0, _EOF)
    
    def closure(self, item_1s):
        for item_1 in item_1s:
            lookahead = item_1.get_lookahead()
            after_position_tokens = item_1.get_after_position()
            if after_position_tokens is _EPSILON:
                raise NotImplemented
            first_token = after_position_tokens[0]
            last_tokens = after_position_tokens[1:] + item_1.get_lookhead()
            if first_token in _NON_TERMINALS :
                production = self.productions_dict[first_token]
                for i in range(len(production)):
                    # 不能包括 B -> @ 
                    new_item = Item_1(production[i], 0, lookahead)
                    item_1s.add(new_item)
                
                first_token_first_set = self.grammar.first(first_token)
                if _EPSILON in first_token_first_set:


        return 

    
    def compute_lr1_sets(self):
        raise NotImplemented
    
    def build_lr1_parsing_table(self):
        raise NotImplemented
    
    def parse(self, input):
        raise NotImplemented