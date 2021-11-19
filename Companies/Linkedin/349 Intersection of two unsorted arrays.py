'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

# https://leetcode.com/problems/intersection-of-two-arrays/discuss/82006/Four-Python-solutions-with-simple-explanation

class Solution:  # O(nlogn + mlogm) Time and O(1) Space.
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        m, n = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = set()
        
        # follow-up: if both arrays pre-sorted
        # ANS: without overlapped, only scan on array, O(n). ave: O(n + m) time and O(1) space
        
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return list(res)


class Solution(object):  # O(m + n) Time and O(n) Space 
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        
        return res