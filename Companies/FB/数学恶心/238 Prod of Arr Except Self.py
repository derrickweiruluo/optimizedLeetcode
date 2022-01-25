'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n
        
        leftProd, rightProd = 1, 1
        for i in range(n):
            j = -1 - i
            res[i] *= leftProd
            res[j] *= rightProd

            # leftProd is always one position behind i index, like prefixproduct
            # rightProd is always one position behind j index, like prefixproduct
            # below both are lagging the res[i], res[j] building
            leftProd *= nums[i]
            rightProd *= nums[j]
        
        return res

# leftProd is always one position behind i index, like prefixproduct
# rightProd is always one position behind j index, like prefixproduct