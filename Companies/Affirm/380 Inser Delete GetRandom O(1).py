'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

'''

import random
class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            idx = len(self.lst)
            self.dic[val] = idx
            self.lst.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            idx = self.dic[val]
            last_elem = self.lst[-1]
            self.dic[last_elem] = idx
            self.lst[idx] = last_elem
            del self.dic[val]
            self.lst.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.lst)