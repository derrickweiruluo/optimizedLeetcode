'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104


##### 
先按照end time sort intervals, 然后update prev_end
loop, 
if: prev_end <= cur start, update prev_end
else: count += 1

https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python
https://docs.google.com/presentation/d/1RGF03Syyw2rhU7MojUWT3G-ejw8NFHEANbgnY2AuDEo/edit#slide=id.g8883765d9c_0_30
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        if n == 1 or n == 0:
            return 0
        
        intervals.sort(key = lambda x: x[1])
        res = 0
        prev_end = -math.inf
        
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
        
        return res
        
