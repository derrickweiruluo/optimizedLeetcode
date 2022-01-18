import collections


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.dic = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.dic[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.dic[val]) == 1
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.dic[val]: return False
        # hashset random popping
        last_elem, idx = self.lst[-1], self.dic[val].pop()


        self.lst[idx] = last_elem
        self.dic[last_elem].add(idx)
        self.dic[last_elem].remove(len(self.lst)-1)
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.lst)
