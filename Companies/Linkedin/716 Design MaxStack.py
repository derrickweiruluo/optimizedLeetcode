
'''
NOTE for 最优解 N/A for Python
Using structures like Array or Stack will never let us popMax quickly. We turn our attention to tree and linked-list structures that have a lower time complexity for removal, with the aim of making popMax faster than O(N)O(N) time complexity.

Say we have a double linked list as our "stack". This reduces the problem to finding which node to remove, since we can remove nodes in O(1)O(1) time.

We can use a TreeMap mapping values to a list of nodes to answer this question. TreeMap can find the largest value, insert values, and delete values, all in O(\log N)O(logN) time.

'''

class MaxStack:

    def __init__(self):
        # stack of [(cur_Val, maxIdx)]
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
        nextMax = self.stack[self.stack[maxIdx - 1][1]][0] if maxIdx != 0 else -math.inf
        for i in range(maxIdx, len(self.stack) - 1):
            if self.stack[i + 1][0] >= nextMax:
                nextMax = self.stack[i + 1][0]
                self.stack[i] = (self.stack[i + 1][0], i)
            else:
                self.stack[i] = (self.stack[i + 1][0], self.stack[i - 1][1])
        self.stack.pop()
        return res