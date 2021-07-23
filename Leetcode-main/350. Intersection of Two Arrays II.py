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
