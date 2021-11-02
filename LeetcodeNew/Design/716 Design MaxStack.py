

class MaxStack:

    def __init__(self):
        # stack of (cur_Val, maxIdx)
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack and x >= self.stack[self.stack[-1][1]][0]:
            idx = len(self.stack)
        else:
            if self.stack:
                idx = self.stack[-1][1]
            else:
                idx = 0
        self.stack.append((x, idx))
    
    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]
        
    def peekMax(self) -> int:
        return self.stack[self.stack[-1][1]][0]        

    def popMax(self) -> int:
        maxIdx = self.stack[-1][1]
        res = self.stack[maxIdx][0]
        nextMax = self.stack[self.stack[maxIdx -1][1]][0] if maxIdx else -math.inf
        
        for i in range(maxIdx, len(self.stack) - 1):
            if self.stack[i + 1][0] >= nextMax:
                nextMax = self.stack[i + 1][0]
                self.stack[i] = (self.stack[i + 1][0], i)
            else:
                self.stack[i] = (self.stack[i + 1][0], self.stack[i - 1][1])
        self.stack.pop()
        
        return res