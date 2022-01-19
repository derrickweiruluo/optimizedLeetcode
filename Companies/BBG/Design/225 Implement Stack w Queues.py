'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
'''

class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        # Pushes element x to the top of the stack.
        self.queue.append(x)
        for _ in range(len(self.queue) - 1): #重组queue，这一步最关键
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # Removes the element on the top of the stack and returns it.
        res = self.queue.popleft()
        return res

    def top(self) -> int:
        # Returns the element on the top of the stack.
        return self.queue[0]

    def empty(self) -> bool:
        #Returns true if the stack is empty, false otherwise.
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()