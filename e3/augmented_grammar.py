from ..e2.grammar import Grammar
from ..e2.production import Production
class AugmentedGrammar(Grammar):
    def __init__(self, productions, start):
        super.__init__(productions)
        self.start = start
    
    def get_start(self):
        return '~'
    
    def get_start_production(self):
        return Production('~', self.start)
