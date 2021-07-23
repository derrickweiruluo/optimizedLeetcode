import bisect
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # 自己想的solution 1， time NlogN
#         res = []
        
#         for i, num in enumerate(nums):
#             idx = bisect_left(res, num)
#             if idx == len(res):
#                 res.append(num)
#                 if len(res) > 2:
#                     return True
#             else:
#                 res[idx] = num
        
#         return False

        # 大神想的 time O(N), 妙妙妙
        doublet = [math.inf] * 2
        
        for num in nums:
            if num < doublet[0]: 
                doublet[0] = num
            if num > doublet[0] and num < doublet[1]: 
                doublet[1] = num
            if num > doublet[1]:
                return True
        
        return False
        
