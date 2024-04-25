type_dic = [
    '关键字', 
    '分界符',
    '运算符',
    '关系运算符',
    '常数', 
    '标识符', 
    ]

class Token():
    def __init__(self, row, col, text='', type_number=1):
        self.text = text
        self.row = row
        self.col = col
        self.type_number = type_number
        self.type = type_dic[type_number-1]
        self.attribute = self.text
    
    def error(self):
        self.attribute = "Error"
        self.type = "Error"
        
    def __str__(self) -> str:
        """
        >>> print(Token(1,1,'3', 3))
        3 (3, 3) 常数 (1, 1)
        >>> print(Token(1,8,'d', 2))
        d (2, d) 标识符 (1, 8)
        >>> print(Token(8,1,';', 5))
        ; (5, ;) 分界符 (8, 1)
        """
        res = ''
        res += self.text
        res += '\t'
        if self.attribute == "Error":
            res += self.attribute
        else:
            res += f'({self.type_number}, {self.attribute})'
        res += '\t'
        res += self.type
        res += '\t'
        res += f'({self.row}, {self.col})'
        return res
    

    def __len__(self) -> int:
        return len(self.text)
