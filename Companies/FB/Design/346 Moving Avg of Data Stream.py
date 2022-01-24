'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

1.  MovingAverage(int size) Initializes the object with the size of the window size.
2.  double next(int val) Returns the moving average of the last size values of the stream.

'''



# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.lst = [0] * size
        self.total = 0
        self.idx = 0
        self.size = size

    def next(self, val: int) -> float:

        self.idx += 1
        self.total -= self.lst[self.idx % self.size]
        self.lst[self.idx % self.size] = val
        self.total += val
        return self.total / min(self.size, self.idx)