'''
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.



Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Input: nums = [23,2,6,4,7], k = 6
Output: true
'''

# Corner case: An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefixRem = {}
        # prefixRem = collections.defaultdict(list)
        prefixRem[0] = -1
        curRem = 0
        
        for i, num in enumerate(nums):
            curRem = (curRem + num) % k
            if curRem in prefixRem: 
                if i - prefixRem[curRem] > 1:
                    return True
                # if curRem == 0 and i != 0:
                #     return True
            else:
                prefixRem[curRem] = i
        
        return False