class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque(maxlen = size)
        # Deque 大法好

    def next(self, val: int) -> float:

        queue = self.queue
        queue.append(val)
        return (sum(queue) / len(queue))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
