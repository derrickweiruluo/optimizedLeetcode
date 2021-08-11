"""
#####
Bisect, Binary Search, Sort
NlogN

You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
The right interval for an interval i is an interval j such that startj >= endi and startj is minimized.
Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 
Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

"""

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        ints = sorted([start, end, idx] for idx, [start, end] in enumerate(intervals))
        
        starts = [i for i,_,_ in ints]
        res = [-1] * len(starts)
        
        for start, end, idx in ints:
            left_pos = bisect.bisect_left(starts, end)
            if left_pos < len(starts):
                res[idx] = ints[left_pos][2]
        
        return res
