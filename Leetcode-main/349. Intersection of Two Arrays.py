class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        len1, len2 = len(nums1), len(nums2)
        
        sortedNums1 = sorted(nums1)
        sortedNums2 = sorted(nums2)
        
        print(sortedNums1)
        print(sortedNums2)
        
        p1 = p2 = 0
        
        res = set()
        
        while p1 < len1 and p2 < len2:
            if sortedNums1[p1] == sortedNums2[p2]:
                res.add(sortedNums1[p1])
                p1 += 1
                p2 += 1
            elif sortedNums1[p1] < sortedNums2[p2]:
                p1 += 1
            else:
                p2 += 1
            
        return res
