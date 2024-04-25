from initial import _NON_TERMINALS, _TERMINALS, _EPSILON
from production import Production

"""
暂时假定终结符和非终结符都是一个字符
"""

class MProduction(Production):
    # 暂时设置只能从Production构造MProduction
    def __init__(self, productions):
        if productions is None:
            raise ValueError(f"'productions' is None")
        self.left = productions[0].get_left()
        self.right = []
        for production in productions:
            self.right.append(production.get_right())

    

    # def __contains__(self, non_terminal):


    def __str__(self):
        left = self.left
        mid = ' -> '
        right = ''
        for right_part in self.right:
            for single in right_part:
                right += single
            right += ' | '
        right = right[:-3]

        return left + mid + right