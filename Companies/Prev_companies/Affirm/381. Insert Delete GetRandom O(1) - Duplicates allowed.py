'''
HR轮后第一轮电面，对面是affirm的一名tech lead。
题很简单，要implement一个randomMap class
需要支持的api是

put, 
get, 
remove,
get_random_uniqueValue‌‌‌‌‌‌‌
get_random_value_by_freq
'''

class RandomizedCollection:

    def __init__(self):
        
        # list of all value
        # hashtable of {val: set of occurred indexes}

        self.lst = []
        self.dic = collections.defaultdict(set) # using set for random set.pop()

    def insert(self, val: int) -> bool:
        """
        insert a value, if Exist? False : True
        """
        self.dic[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.dic[val]) == 1 # 新的，len = 1， True， else False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.dic[val]: return False

        # dic[val].pop() 随机remove他的一个index
        last_elem, idx = self.lst[-1], self.dic[val].pop() 
        self.lst[idx] = last_elem
        self.dic[last_elem].add(idx)
        self.dic[last_elem].remove(len(self.lst)-1) # remove the lastIdx belong the suffled elem
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        
        # return a random_val by frequency
        return choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()