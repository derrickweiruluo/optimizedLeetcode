"""
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109


#########
Sliding window implementation with increasing deque, deque of [idx, cur_sum]
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        queue = collections.deque([[0, 0]])
        res, cur_sum = math.inf, 0
        
        for i, num in enumerate(nums):
            cur_sum += num
            while queue and cur_sum - queue[0][1] >= k:
                res = min(res, i + 1 - queue.popleft()[0])
            while queue and cur_sum <= queue[-1][1]:
                queue.pop()
            queue.append([i + 1, cur_sum])
        
        return res if res != math.inf else -1
