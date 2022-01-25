'''
You are given an inclusive range [lower, upper] 
and a sorted unique integer array nums, where all elements are in the inclusive range.
'''

# nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: ["2","4->49","51->74","76->99"]


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        # given an inclusive range [lower, upper]
        # num: a sorted unique integer array, , where all elements are in the inclusive range.
        # lower <= nums[0], nums[-1] <= upper
        
        '''
             0, 1, 3,  50,   75    idx_n
        L    -1 1  2   4     51     76
        R    -1 0  2   49    74     99
        add   N N  Y   Y     Y
        diff  0    2  4-49  51-74  76-99
        
        '''
        
        res = []
        n = len(nums)
        for i in range(n + 1):
            # left is prev + 1, right is cur - 1, find gap in btw
            left = lower if i == 0 else nums[i - 1] + 1
            right = upper if i == n else nums[i] - 1

            if left < right:
                res.append(str(left) + '->' + str(right))
            if left == right:
                res.append(str(left))
            
        return res
        
        
#         nums = [lower - 1] + nums + [upper + 1]
#         res = []
        
#         for i in range(len(nums) - 1):
#             if nums[i + 1] - nums[i] == 2:
#                 res.append(str(nums[i] + 1))
#             elif nums[i + 1] - nums[i] > 2:
#                 res.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))
        
#         return res