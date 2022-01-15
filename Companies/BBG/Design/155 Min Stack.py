
# BEST, both solution is O(1) time in all functions
class Node: 
    def __init__(self, val, minVal, prev):
        self.val = val
        self.minVal = minVal
        self.prev = prev

class MinStack:

    def __init__(self):

        # this head node is dynamically changing as we popTop, or insert new
        self.head = Node(0, math.inf, None)
        
    def push(self, val: int) -> None:

        # new head is create with the new Val and minVal, and point to head
        # and this head is the updated head
        self.head = Node(val, min(val, self.head.minVal), self.head)

    def pop(self) -> None:
        self.head = self.head.prev

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.minVal




#* ------------------
class MinStack:

    def __init__(self):
        self.stack = []   # stack of curVal, stackMaxVal

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]