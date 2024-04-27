from ..e2.production import Production
from ..e2.initial import _EPSILON

class Item(object):
    def __init__(self, production, position: int):
        self.production = production
        self.position = position
    
    def __str__(self) -> str:
        left = self.production.get_left()
        mid = " -> "
        right = self.production.get_right()
        right = right[0: self.position] + ' · ' + right[self.position:]
        return left + mid + right

    def __repr__(self) -> str:
        left = self.production.get_left()
        mid = " -> "
        right = self.production.get_right()
        right = right[0: self.position] + ' · ' + right[self.position:]
        return left + mid + right

    def __hash__(self):
        return self.__hash__()

    def __eq__(self, other_item) -> bool:
        return self.position == other_item.get_position() \
              and self.get_production() == other_item.get_production()
    
    def get_production(self) -> Production:
        return self.production
    
    def get_position(self) -> int:
        return self.position

    def get_after_position(self):
        right = self.production.get_right()
        if self.position == len(right):
            return _EPSILON
        return right[self.position:]