"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.kth(nums1, nums2, n // 2)
        else:
            return (self.kth(nums1, nums2, n // 2 - 1) + self.kth(nums1, nums2, n // 2)) / 2
        
    def kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        i, j = len(nums1) // 2, len(nums2) // 2
        med_1, med_2 = nums1[i], nums2[j]
        
        if i + j < k:
            if med_1 > med_2:
                return self.kth(nums1, nums2[j + 1:], k - j - 1)
            else:
                return self.kth(nums1[i + 1:], nums2, k - i - 1)
        else:
            if med_1 > med_2:
                return self.kth(nums1[:i], nums2, k)
            else:
                return self.kth(nums1, nums2[:j], k)
