class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        '''
        bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        '''
        if val not in self.dic:
            idx = len(self.lst)
            self.dic[val] = idx
            self.lst.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        '''
        Removes an item val from the set if present. 
        Returns true if the item was present, false otherwise
        '''
        if val in self.dic:
            last_elem, idx = self.lst[-1], self.dic[val]
            self.dic[last_elem] = idx
            self.lst[idx] = last_elem
            self.dic.pop(val)
            self.lst.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        '''
        Returns a random element from the current set of elements
        Valid call, each elem should have the same probability
        '''
        return random.choice(self.lst)