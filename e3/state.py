class State(object):
    def __init__(self, index, item_1s=None, next_state_dict=None):
        self.item_1s = item_1s
        self.next_state_dict = next_state_dict
    
    def __getitem__(self, input):
        if input not in self.next_state_dict.keys():
            raise KeyError(f"{input} is not a correct input")
        return self.next_state_dict[input]

