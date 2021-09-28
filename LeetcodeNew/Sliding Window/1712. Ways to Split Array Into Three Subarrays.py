'''
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.


Input: nums = [1,1,1]
Output: 1

Input: nums = [1,2,2,2,5,0]
Output: 3
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]

Input: nums = [3,2,1]
Output: 0

#######
First, we prepare the prefix sum array, so that we can compute subarray sums in O(1). Then, we move the boundary of the first subarray left to right. This is the first pointer - i.

For each point i, we find the minimum (j) and maximum (k) boundaries of the second subarray:

https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/discuss/999257/C%2B%2BJavaPython-O(n)-with-picture
'''

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        res = 0 
        j, k = 0, 0
        n = len(nums)
        preSum = nums
        for i in range(1, len(nums)):
            preSum[i] += preSum[i - 1]
        
        """j, k is the left bound and right bound of the second array
        in preSum array, preSum[i] is firstSum, preSum[j/k] - preSum[i] is secondSum, preSum[-1] - preSum[j/k] is thirdSum"""
        
        for i in range(n - 2):
            while j <= i or j < n - 1 and preSum[j] < preSum[i] * 2:
                j += 1
            while k < j or k < n - 1 and preSum[-1] - preSum[k] >= preSum[k] - preSum[i]:
                k += 1
            window = k - j 
            res = (res + window) % (10 ** 9 + 7)
        
        return res
