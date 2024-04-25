class Table:
    def __init__(self, table_name='', table_keys=[], table_items=[]):
        self.table_name = table_name
        self.table_keys = table_keys
        self.table_items = table_items
    
    def append(self, table_key, table_item):
        """
        >>> a = Table('', [1, 2, 3], [4, 5, 6])
        >>> a.append(4, 7)
        >>> a[3]
        (4, 7)
        """
        if table_key is None:
            raise KeyError(f"table_key is None")
        if len(self) > 0 and table_key in self.table_keys:
            raise KeyError(f"{table_key} already existed")
        if table_item is None:
            raise TypeError(f"table_item is None")
        if len(self) > 0 and table_item in self.table_items:
            raise TypeError(f"{table_item} already existed")
        self.table_keys.append(table_key)
        self.table_items.append(table_item)
    
    def __getitem__(self, k):
        """
        >>> a = Table('', [1, 2, 3], [4, 5, 6])
        >>> a[0]
        (1, 4)
        >>> a[1]
        (2, 5)
        """
        if k < 0:
            raise IndexError(f"negative index to < Table {self.table_name}>")
        if k >= len(self):
            raise IndexError(f"out index of < Table {self.table_name}>")
        
        return self.table_keys[k], self.table_items[k]
    
    def __contains__(self, item):
        """
        >>> a = Table('', [1,2,3], [4,5,6])
        >>> 4 in a
        True
        >>> 5 in a
        True
        >>> 9 in a
        False
        """
        if len(self) == 0:
            return False
        return item in self.table_items
    
    def __len__(self):
        """
        >>> a = Table('', [1,2,3], [4,5,6])
        >>> len(a)
        3
        """
        if self.table_keys is None:
            return 0
        return len(self.table_keys)
