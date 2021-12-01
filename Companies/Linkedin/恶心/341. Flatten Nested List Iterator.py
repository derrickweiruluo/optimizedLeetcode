'''
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
'''
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList): # : [NestedInteger]
        self.queue = collections.deque(nestedList)
    
    def next(self) -> int:
        return self.queue.popleft().getInteger()
    
    def hasNext(self) -> bool:
        while self.queue:
            top = self.queue[0]
            if top.isInteger():
                return True
            # if top of the stack is a nested List, keep unzip it
            # we ONLY manipulate the top of the stack
            top = self.queue.popleft().getList()
            self.queue.extendleft(top[::-1])
        return False


class NestedIterator: # stack
    def __init__(self, nestedList): #NestedInteger
        self.stack = nestedList
    
    def next(self) -> int:
        return self.stack.pop(0).getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[0]
            if top.isInteger():
                return True
            self.stack = top.getList() + self.stack[1:]
        return False