'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
'''

 #Greedy
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        curEnd = -math.inf

        # greedy sort, sort by end time, 这样可以腾出更多的空间来维持不重叠
        intervals.sort(key = lambda x: x[1])

        for start, end in intervals:
            if start >= curEnd:
                curEnd = end
            else:
                res += 1
        
        return res