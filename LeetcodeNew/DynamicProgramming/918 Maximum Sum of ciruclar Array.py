'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
'''

'''
Explanation
So there are two case.
Case 1. The first is that the subarray take only a middle part, and we know how to find the max subarray sum.
Case2. The second is that the subarray take a part of head array and a part of tail array.
We can transfer this case to the first one.

The maximum result equals to the (totalSum -  minimum subarray sum).

Corner case
Just one to pay attention:
If all numbers are negative, maxSum = max(A) and minSum = sum(A).
In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
According to the deacription, We need to return the max(A), instead of sum of am empty subarray.
So we return the maxSum to handle this corner case.
'''
# 看lee神的图讲解两种 max subarray
class SolutionLee:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total, curMin, curMax = 0, 0, 0
        maxSum, minSum = nums[0], nums[0]
        
        for num in nums:
            # 前两行, Case 1, max subarray不跨越：计算max subarray
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            # 后两行，Case 2, max subarray跨越边界：处理min subarray
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
        
        # corner case： 全负数，maxSum就是最大
        if maxSum < 0:
            return maxSum

        return max(maxSum, sum(nums) - minSum)