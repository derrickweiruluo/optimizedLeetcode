"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

########
前向和之差为k的时候，count += [cur_sum - k]

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        running_sum, count = 0, 0
        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] = 1
        
        for num in nums:
            running_sum += num
            count += prefix_sum[running_sum - k]
            prefix_sum[running_sum] += 1
        
        return count
