
# Explanation of the problem
''' 
Basically , we need to store every incoming value at the given index. And
with every incoming index, we have to check

If the current index is less than the incoming index, the we have to return
an empty list

Else , we have to return an sliced list from the incoming index to the first index
where there is no insertion till yet.
'''

class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0 # 0-indexed

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.data[idKey] = value
        if idKey > self.ptr:
            return []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1 # update ptr
        return self.data[idKey: self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)