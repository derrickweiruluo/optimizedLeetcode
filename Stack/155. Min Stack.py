'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''

class MinStack:

    def __init__(self):
        self.stack = []  # stack of [cur_val, min_val]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            if val > self.stack[-1][1]:
                self.stack.append((val, self.stack[-1][1]))
            else:
                self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()