
# BEST, both solution is O(1) time in all functions
class Node: 
    def __init__(self, val, minVal, prev):
        self.val = val
        self.minVal = minVal
        self.prev = prev

class MinStack:

    def __init__(self):
        self.head = Node(0, math.inf, None)
        
    def push(self, val: int) -> None:
        # pushes the element val onto the stack.
        self.head = Node(val, min(val, self.head.minVal), self.head)

    def pop(self) -> None:
        # removes the element on the top of the stack.
        self.head = self.head.prev

    def top(self) -> int:
        # gets the top element of the stack.
        return self.head.val

    def getMin(self) -> int:
        # retrieves the minimum element in the stack.
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