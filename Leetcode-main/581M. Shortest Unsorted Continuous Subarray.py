class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        enum = enumerate(zip(sorted(nums),nums))
        res = [i for (i, (a, b)) in enum if a != b]
        if not res: 
            return 0
        else:
            return res[-1] - res[0] + 1
          

          
# # 新用法 zip(nums_1, nums_2)

        # nums = [1,2,3,5,4]
        # s =    [1,2,3,4,5]
        # enum = enumerate(zip(nums, s))
        # print (list(enum))

# # result:
# #[(0, (1, 1)), (1, (2, 2)), (2, (3, 3)), (3, (5, 4)), (4, (4, 5))]
