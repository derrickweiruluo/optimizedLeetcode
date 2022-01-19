'''
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.
'''

'''
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.


Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
'''



class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        intervals = sorted([start, end, idx] for idx, [start, end] in enumerate(intervals))
        
        startIdxes = [startVal for startVal, end, idx in intervals]
        res = [-1] * len(startIdxes)
        
        for start, end, idx in intervals:
            # left_pos = bisect.bisect_left(startIdxes, end)
            left_pos = self.binarySearchLeft(startIdxes, end)
            if left_pos < len(startIdxes):
                res[idx] = intervals[left_pos][2]
        
        return res

    
    def binarySearchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left if left < len(nums) else len(nums)