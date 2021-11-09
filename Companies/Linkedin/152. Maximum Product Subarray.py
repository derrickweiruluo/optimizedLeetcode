'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.'''

class Solution1:  # Optimized, O(1) Time
    def maxProduct(self, nums: List[int]) -> int:
        
        # O(N) time and O(1) Space
        prefix, suffix, res = 0, 0, -math.inf
        n = len(nums)
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n - 1 - i]
            res = max(res, prefix, suffix)
        
        return res
            
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(N) space and time
        prefix = nums
        suffix = nums[::-1]
        for i in range(1, len(nums)):
            prefix[i] *= (prefix[i - 1] or 1)
            suffix[i] *= (suffix[i - 1] or 1)
        
        return max(prefix + suffix)
        
#         prefixNums = nums
#         suffixNums = nums[::-1]
        
#         for i in range (1, len(nums)):
#             prefixNums[i] = prefixNums[i] * (prefixNums[i - 1] or 1)
#             suffixNums[i] = suffixNums[i] * (suffixNums[i - 1] or 1)
        
        '''
        PrefixArray: [2,3,-2,4]
        SuffixArray: [4,-2,3,2]
        
        at idx = 0, prefix = 2,        suffix = 4              
        at idx = 1, prefix = 2*3       suffix = 4*-2        
        at idx = 2, prefix = 2*3*-2    suffix = 4*-2*3      
        at idx = 3, prefix = 2*3*-2*4  suffix = 4*-2*3*2
        '''
        
        


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefix = nums
        suffix = nums[::-1]
        
        for i in range(1, len(nums)):   # calculate prefix and suffix sum
            prefix[i] = prefix[i] * (prefix[i - 1] or 1)  # or 1 means the product of itself 
            suffix[i] = suffix[i] * (suffix[i - 1] or 1)
        
        return max(prefix + suffix)
