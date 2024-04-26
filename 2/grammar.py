from production import Production
from mproduction import MProduction
from initial import _TERMINALS, _NON_TERMINALS, _EPSILON, _EOF, _START_SYMBOLS

class Grammar(object):
    def __init__(self, productions):
        if productions is None:
            raise ValueError("productions is None")
        # 没有实现对 productions 的详细检查
        self.productions = {}
        for production in productions:
            if production.get_left() in self.productions.keys():
                raise ValueError(f"{production}'s left \
                                 '{production.get_left()} has already existed")
            self.productions[production.get_left()] = production
        
        # first 和 follow 先不初始化，只有在使用 get 的时候才初始化
        self.first_sets = {}
        self.follow_sets = {}
        
    
    def get_productions(self):
        return self.productions.values()
    

    def get_first_sets(self) -> dict:
        """
        获取 first 集"""
        if len(self.first_sets) == 0:
            self.first_sets = self._create_first_sets()
        return self.first_sets
    
    def _create_first_sets(self) -> dict:
        first_sets = {}
        productions = self.get_productions()
        for production in productions:
            non_terminal = production.get_left()
            first_sets[non_terminal] = self._first(non_terminal)
        return first_sets
    
    def _first(self, non_terminal) -> set :
        """
        获取某个非终结符的 first 集"""
        if non_terminal not in self.productions.keys():
            raise ValueError(f"{non_terminal} is not in Grammar")
        
        first_set = set()
        cur_production = self.productions[non_terminal]
        for right_parts in cur_production.get_right():
            if right_parts[0] in _TERMINALS:
                first_set.add(right_parts[0])
            elif right_parts[0] in _NON_TERMINALS:
                sub_set = self._first(right_parts[0])
                first_set = first_set.union(sub_set)
                if _EPSILON in sub_set:
                    if len(right_parts) > 1:
                        first_set = first_set.union(self._first(right_parts[1]))
            elif right_parts[0] in _EPSILON:
                first_set.add(_EPSILON)
        return first_set
        

    def get_follow_sets(self):
        """
        获取 follow 集"""
        if len(self.first_sets) == 0:
            self.get_first_sets()
        if len(self.follow_sets) == 0:
            self.follow_sets = self._create_follow_sets()
        return self.follow_sets
    
    def _create_follow_sets(self) -> dict:
        """
        创建 follow 集合"""
        follow_sets = {}
        productions = self.get_productions()
        for production in productions:
            non_terminal = production.get_left()
            follow_sets[non_terminal] = self._follow(non_terminal)
        return follow_sets

            
    def _follow(self, cur_non_terminal):
        """
        获取某个非终结符的 follow 集"""
        follow = set()
        if cur_non_terminal in _START_SYMBOLS:
            follow.add(_EOF)
        
        productions = self.get_productions()
        for production in productions:
            non_terminal, right = production.get_left(), production.get_right()
            for right_part in right:
                for char in right_part:
                    if char == cur_non_terminal:
                        follow_s = right_part[right_part.index(char) + 1:]
                        # A -> aB
                        if len(follow_s) == 0:
                            if cur_non_terminal == non_terminal:
                                continue
                            else:
                                # print('yes')
                                follow = follow | \
                                    self._follow(non_terminal)

                        # A -> aBb
                        else:
                            follow_2 = set()
                            for s in follow_s:
                                if s in _TERMINALS:
                                    follow_2.add(s)
                                    break
                                else:
                                    first_set = self.get_first_sets()[s]
                                    if _EPSILON in first_set:
                                        follow_2 = follow_2 | first_set - \
                                            {_EPSILON}
                                        if s is follow_s[-1]:
                                            follow_2 = follow_2 | self._follow(non_terminal)
                                    else:
                                        follow_2 = follow_2 | first_set
                                        break
                            follow = follow | follow_2
        # print(cur_non_terminal, " ", "follow done")
        return follow


    
    @property
    def is_left_recursion(self):
        raise NotImplemented

    @property
    def is_LL(self):
        raise NotImplemented

def create_grammar(lines: list) -> Grammar:
    productions = []
    mproductions = []
    
    cur_non_terminal = lines[0][0]
    for line in lines:
        line = line.rstrip()
        left = line[0]
        right = line[2:]
        if left != cur_non_terminal:
            mproduction = MProduction(productions.copy())
            mproductions.append(mproduction)
            productions = []
            cur_non_terminal = left
        production = Production(left, right)
        productions.append(production)
    
    if productions is not []:
        mproduction = MProduction(productions)
        mproductions.append(mproduction)
    
    # print(mproductions)

    return Grammar(mproductions)