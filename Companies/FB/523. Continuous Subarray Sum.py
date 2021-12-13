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

"""
题目大意：
求数组nums中是否存在k的整数倍，并且长度至少为2的连续子段和。
注意：
数组长度不超过10,000。
可以假设所有数字的和范围在32位带符号整数之内。
解题思路：
遍历数组nums，求前i项和total；对k取模，记模值为m
利用map[m]记录模为m的前i项和的最小下标，初始令map[0] = -1
若map[m] + 1 < i，则返回True
"""


'''
0 <= nums[i] <= 10^9
'''
# Time complexity: O(n), 
# space complexity: O(min(k, n)) if k != 0, else O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefixRem = 0
        seen = collections.defaultdict(list)
        seen[0].append(-1)
        
        for idx, num in enumerate(nums):
            prefixRem = (prefixRem + num) % k
            if prefixRem in seen:
                if idx - seen[prefixRem][-1] > 1:
                    # print(idx, seen[prefixRem][-1])
                    return True
            else:
                seen[prefixRem].append(idx)
        
        return False