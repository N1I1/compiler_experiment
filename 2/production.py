from initial import _NON_TERMINALS, _TERMINALS, _EPSILON

class Production(object):
    def __init__(self, left, right_part):
        if left is None:
            raise ValueError(f"left is None")
        if right_part is None:
            raise ValueError(f"right is None")
        if left not in _NON_TERMINALS:
            raise TypeError(f"{left} is not a Non_Terminal")
            
        self.left = left
        self.right = []
        for right in right_part:
            if right not in _TERMINALS and right not in _NON_TERMINALS and right not in _EPSILON:
                raise TypeError(f"{right} can't be the right of Production")
            self.right.append(right)

    def __str__(self) -> str:
        right = ''
        for right_part in self.get_right():
            right += right_part
        return self.get_left() + " -> " + right
    
    def __contains__(self, s) -> bool:
        return s in self.get_right()
    
    def __hash__(self) -> int:
        return self.__hash__()
    
    def __eq__(self, other_production) -> bool:
        return self.left == other_production.get_left()
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right