'''
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule()   Initializes the object of the data structure.

void addRange(int left, int right)  Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.

boolean queryRange(int left, int right)     Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.

void removeRange(int left, int right)   Stops tracking every real number currently being tracked in the half-open interval [left, right).
'''


import bisect

class RangeModule:

    def __init__(self):
        self.nums = []

    def addRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.nums, left)
        j = bisect.bisect_right(self.nums, right)
        self.nums[i: j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)
        
    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.nums, left)
        j = bisect.bisect_left(self.nums, right)
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.nums, left)
        j = bisect.bisect_right(self.nums, right)
        self.nums[i: j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)
