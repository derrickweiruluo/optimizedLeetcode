'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
'''


# FOLLOW UP
# 1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?

# We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle value to get our median.
# Time and space complexity would be O(100) = O(1).


# 2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

# As 99% is between 0-100. So can keep a counter for less_than_hundred and greater_than_hundred.
# As we know soluiton will be definately in 0-100 we don't need to know those number which are >100 or <0, only count of them will be enough.



import heapq
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