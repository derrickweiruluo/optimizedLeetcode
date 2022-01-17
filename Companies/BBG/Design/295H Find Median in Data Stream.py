'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
'''

class MedianFinder:

    def __init__(self):
        # left 存负数, heap pop出来的左边最大值
        # right 存 正数, heap pop出来右边最小值
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # adds the integer num from the data stream to the data structure.
        heapq.heappush(self.left, -1* heapq.heappushpop(self.right, num))
        if len(self.left) > len(self.right):
            val = heapq.heappop(self.left) * (-1)
            heapq.heappush(self.right, val)

    def findMedian(self) -> float:
        # returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.s
        if len(self.left) < len(self.right):
            return self.right[0]
        else:
            # left 存负数, heap pop出来的左边最大值
            # right 存 正数, heap pop出来右边最小值
            return self.right[0] / 2.0 - self.left[0] / 2.0
            # return (self.right[0] - self.left[0]) / 2.0