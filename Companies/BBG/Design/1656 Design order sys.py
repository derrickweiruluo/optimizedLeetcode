
# Explanation of the problem
''' 
Basically , we need to store every incoming value at the given index. And
with every incoming index, we have to check

If the current index is less than the incoming index, the we have to return
an empty list

Else , we have to return an sliced list from the incoming index to the first index
where there is no insertion till yet.
'''
class OrderedStream:   # 一毛一样的解法

    def __init__(self, n: int):
        self.data = [None] * n
        # self.ptr = 0

        # is always advancing, so that the past return values
        # wont return again, only the previous un-returned results
        self.pointer = 0 

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey - 1] = value
        res = []
        while self.pointer < len(self.data) and self.data[self.pointer]:
            res.append(self.data[self.pointer])
            self.pointer += 1
        return res





class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0 # 0-indexed

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  # 0 index
        self.data[idKey] = value
        if idKey > self.ptr:
            return []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1 # update ptr if it has been filled by previous insertions
        return self.data[idKey: self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)