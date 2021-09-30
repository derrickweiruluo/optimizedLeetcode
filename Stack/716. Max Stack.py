"""
MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

Constraints:

-107 <= x <= 107
At most 104 calls will be made to push, pop, top, peekMax, and popMax.
There will be at least one element in the stack when pop, top, peekMax, or popMax is called.
 
Follow up: Could you come up with a solution that supports O(1) for each top call and O(logn) for each other call? 

"""
class MaxStack:

    def __init__(self):
        # stack of (cur_val, idx_of_max)
        self.stack = []
        self.time = 0
        
    def push(self, x: int) -> None: # O(logn)
        if self.stack and x >= self.stack[self.stack[-1][1]][0]:
            idx = len(self.stack)
        else:
            idx = self.stack[-1][1] if self.stack else 0
        self.stack.append((x, idx, self.time))
        self.time += 1
        

    def pop(self) -> int: # O(1)
        return self.stack.pop()[0]

    def top(self) -> int:  # O(1)
        return self.stack[-1][0]

    def peekMax(self) -> int: # O(logn)
        return self.stack[self.stack[-1][1]][0]

    def popMax(self) -> int: # O(logn)
        maxIdx = self.stack[-1][1]
        res = self.stack[maxIdx][0]
        
        # below steps is to re-compute the stack from maxIdx to the top of the stack
        nextMax = self.stack[self.stack[maxIdx - 1][1]][0] if maxIdx > 0 else -math.inf
        for i in range(maxIdx, len(self.stack) - 1):
            if self.stack[i + 1][0] >= nextMax:
                nextMax = self.stack[i + 1][0]
                self.stack[i] = (self.stack[i + 1][0], i)
            else:
                self.stack[i] = (self.stack[i + 1][0], self.stack[i - 1][1])
        self.stack.pop()
        
        
        return res