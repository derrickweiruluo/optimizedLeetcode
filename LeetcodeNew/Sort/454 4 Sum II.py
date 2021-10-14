'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

'''

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        leftSum = [a + b for a in nums1 for b in nums2]
        leftSumCounter = collections.Counter(leftSum)
        res = 0
        
        for num3 in nums3:
            for num4 in nums4:
                res += leftSumCounter[0 - num3 - num4]
        
        return res