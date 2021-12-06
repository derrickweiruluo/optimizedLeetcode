class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470959/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100
        
        counter = collections.Counter(changed)
        res = []
        
        if counter[0] % 2: return []
        for key in sorted(counter):
            if counter[key] > counter[key * 2]:
                return []
            if key == 0:
                counter[key] //= 2
            else:
                counter[key * 2] -= counter[key]
        
        print(counter)
        return list(counter.elements())
    
#     Python, O(N + KlogK)
#     LEE 215

#     def findOriginalArray(self, A):
#         c = collections.Counter(A)
#         if c[0] % 2:
#             return []
#         for x in sorted(c):
#             if c[x] > c[2 * x]:
#                 return []
#             c[2 * x] -= c[x] if x else c[x] / 2
#         return list(c.elements())