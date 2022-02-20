'''
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sortedNums1, sortedNums2 = sorted(nums1), sorted(nums2)
        res = []
        
        p1 = p2 = 0
        
        while p1 < len(sortedNums1) and p2 < len(sortedNums2):
            if sortedNums1[p1] < sortedNums2[p2]:
                p1 += 1
            elif sortedNums1[p1] > sortedNums2[p2]:
                p2 += 1
            else:
                res.append(sortedNums1[p1])
                p1 += 1
                p2 += 1
        
        return res


class Solution(object):
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res