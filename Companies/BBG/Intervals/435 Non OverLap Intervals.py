'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2

Input: intervals = [[1,2],[2,3]]
Output: 0
'''

# return # of intervals removed to make the list "Non-Overlapped"

# Greedy + sorting
# sort by end time and remove the earliest one and having a left pointer
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        end = -math.inf
        
        for s, e in sorted(intervals, key = lambda x: x[1]):
            if s >= end:
                end = e
            else:
                res += 1
        
        return res