"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

#############
变形prefix sum
1的话 +1， 0 的话-1
如果某个index里，该prefix sum 在之前出现过，那么 idx - dic[prefixSum] 就是当前解

"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefix_sum = {0: -1}
        cur_sum, maxLen = 0, 0
        
        for i in range(len(nums)):
            cur_sum += nums[i] or -1
            print(cur_sum)
            if cur_sum not in prefix_sum:
                prefix_sum[cur_sum] = i
            else:
                maxLen = max(maxLen, i - prefix_sum[cur_sum])
        
        return maxLen
