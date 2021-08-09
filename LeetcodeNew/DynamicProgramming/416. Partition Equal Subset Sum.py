"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

####
subsum_set and check every num for target


Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100

"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        if sum(nums) % 2 == 1: 
            return False
        target = sum(nums) // 2     #target sum 
        subsums_set = set([0])      #stores the sums of the subsets
        
        for num in nums:
            sum_with_num = []       #stores the sums of the subsets that contain "num"
            for sub_sum in subsums_set:
                if num + sub_sum == target:
                    return True
                if num + sub_sum < target:
                    sum_with_num.append(num + sub_sum)
            
            subsums_set.update(sum_with_num)
        
        return False
