'''152. Maximum Product Subarray
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefixNums = nums
        suffixNums = nums[::-1]
        
        for i in range (1, len(nums)):
            prefixNums[i] = prefixNums[i] * (prefixNums[i - 1] or 1)
            suffixNums[i] = suffixNums[i] * (suffixNums[i - 1] or 1)
        
        '''
        PrefixArray: [2,3,-2,4]
        SuffixArray: [4,-2,3,2]
        
        at idx = 0, prefix = 2,        suffix = 4              
        at idx = 1, prefix = 2*3       suffix = 4*-2        
        at idx = 2, prefix = 2*3*-2    suffix = 4*-2*3      
        at idx = 3, prefix = 2*3*-2*4  suffix = 4*-2*3*2
        '''
        
        return max(prefixNums + suffixNums)