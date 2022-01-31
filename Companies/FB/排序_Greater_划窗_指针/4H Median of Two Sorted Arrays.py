'''
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''


# BEST
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        left, right, median = 0, m, (m + n + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = median - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                left = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                right = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n = len(nums1) + len(nums2)
        # Given two sorted arrays nums1 and nums2
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
        mid1, mid2 = nums1[i], nums2[j]
        if i + j < k:
            if mid1 < mid2:
                return self.kth(nums1[i + 1:], nums2, k - i - 1)
            else:
                return self.kth(nums1, nums2[j + 1:], k - j - 1)
        else:
            if mid1 < mid2:
                return self.kth(nums1, nums2[:j], k)
            else:
                return self.kth(nums1[:i], nums2, k)