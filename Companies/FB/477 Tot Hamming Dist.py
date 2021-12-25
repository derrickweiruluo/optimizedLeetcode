'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

 

Example 1:

Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

'''

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        # 4  is 0100, 
        # 14 is 1110,
        # 2  is 0010
        
        res = 0
        n = len(nums)
        
        # try all combo is TLE
        # for every bit position
        # check how many 1s in all nums
        # cur_bitCount += (n - k) * k
        for j in range(32):
            bitCount = 0
            for i in range(n):
                bitCount += nums[i] >> j & 1
            res += bitCount * (n - bitCount)
        
        
        return res