'''
Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
'''

class MyQueue:  # Two Stacks
                # push O(1), pop amortized O(1)

    #只用两个stack的话，每次运作都把 stack1 的pop掉存进另 stack2
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


class MyQueue(object):  # one stack and recursively call push 
    def __init__(self):
        self.st = []

    def push(self, x):
        if len(self.st) == 0:
            self.st.append(x)
            return
        tmp = self.st.pop(-1)
        self.push(x)
        self.st.append(tmp)

    def pop(self):
        return self.st.pop(-1)

    def peek(self):
        return self.st[-1]

    def empty(self):
        return len(self.st) == 0
