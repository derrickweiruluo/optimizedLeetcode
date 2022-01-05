'''
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

'''


# We iterate through the input array exactly once, 
# keeping track of the running sum mod k of the elements in the process. 
# If we find that a running sum value at index j has been previously seen before in some earlier index i in the array, then we know that the sub-array (i,j] contains a desired sum.

''' Clarifications:
1.  is ZERO a muiltple of k (!!!!!!!)
2.  len of 2 requirement
#   conrner cases: [0,0], for multiplier is zero
'''


class Solution: # 一种 O(K) space 的解法
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
                
                # 额外的check for adjecent zeros
                # 0 is always a multiple of k (给予的条件)
                if curRem == 0 and i != 0: 
                    return True
            else:
                prefixRem[curRem] = i
        
        return False


# Time complexity: O(n), 
# space complexity: O(min(k, n)) if k != 0, else O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        curSum = 0
        prefixRem = collections.defaultdict(list)
        prefixRem[0].append(-1) # initialize 0:-1, in for subarray start from -1
        
        for i, num in enumerate(nums):
            curSum = (curSum + num) % k
            if curSum in prefixRem:
                if i - prefixRem[curSum][-1] > 1:
                    return True
            else:
                prefixRem[curSum].append(i)
        
        return False



