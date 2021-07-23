class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = collections.Counter()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.ds[key] += 1 

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        self.ds[key] -= 1
        if self.ds.get(key,0) == 0:
            del self.ds[key]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if len(self.ds) == 0:
            return ""
        else:
            return self.ds.most_common(1)[0][0]

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if len(self.ds) == 0:
            return ""
        else:
            return self.ds.most_common(len(self.ds))[-1][0]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
