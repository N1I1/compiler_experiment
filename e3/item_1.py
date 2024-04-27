from item import Item
class Item_1(Item):
    def __init__(self, production, position: int, lookahead):
        super(production, position)
        self.lookahead = lookahead

    def __str__(self) -> str:
        return super.__str__() + f', {self.lookahead}'

    def __repr__(self) -> str:
        return super.__repr__() + f', {self.lookahead}'
    
    def __eq__(self, other_item) -> bool:
        return self.production == other_item.production \
            and self.position == other_item.get_position() \
            and self.lookahead == other_item.get_lookahead()
    
    def __hash__(self):
        return super().__hash__()
    
    def get_lookahead(self):
        return self.lookahead
    