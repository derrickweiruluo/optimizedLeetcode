'''
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule()   Initializes the object of the data structure.

void addRange(int left, int right)  Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.

boolean queryRange(int left, int right)     Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.

void removeRange(int left, int right)   Stops tracking every real number currently being tracked in the half-open interval [left, right).
'''



# We make use of the python bisect_left and bisect_right functions. bisect_left returns an insertion index in a sorted array to the left of the search value. bisect_right returns an insertion index in a sorted array to the right of the search value. See the python documentation. To keep track of the start and end values of the ranges being tracked, we use a tracking array of integers. This array consists of a number of sorted pairs of start and end values. So, it always has an even number of elements.

# addRange first gets the leftmost insertion index of the left value and the rightmost insertion index of the right value. Then, we check if either of these indexes are even. If the index is even, it means that it is currently outside the range of start and end indexes being tracked. In this case, we include this index to be updated in the tracking array. We then use python array slicing to overwrite the tracking array with the left and right values placed in the correct index. Complexity is O(n).

# removeRange first gets the leftmost insertion index of the left value and the rightmost insertion index of the right value. Then, we check if either of these indexes are odd. If the index is odd, it means that it is currently inside the range of start and end indexes being tracked. In this case, we include this index to be updated in the tracking array. We then use python array slicing to overwrite the tracking array with the left and right values placed in the correct index. Complexity is O(n).

# queryRange gets the rightmost insertion index of the left value and the leftmost insertion index of the right value. If both these indexes are equal and these indexes are odd, it means the range queried is inside the range of values being tracked. In this case, we return True. Else, we return False. Complexity is O(log n).


import bisect

class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        start = bisect.bisect_left(self.ranges, left)
        end = bisect.bisect_right(self.ranges, right)
        
        newRange = []
        if start % 2 == 0:
            newRange.append(left)
        if end % 2 == 0:
            newRange.append(right)
			
        self.ranges[start:end] = newRange

    def removeRange(self, left, right):
        start = bisect.bisect_left(self.ranges, left)
        end = bisect.bisect_right(self.ranges, right)
        
        newRange = []
        if start % 2 == 1:
            newRange.append(left)
        if end % 2 == 1:
            newRange.append(right)
			
        self.ranges[start:end] = newRange
		
    def queryRange(self, left, right):
        start = bisect.bisect_right(self.ranges, left)
        end = bisect.bisect_left(self.ranges, right)
		
        return start == end and start % 2 == 1





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
