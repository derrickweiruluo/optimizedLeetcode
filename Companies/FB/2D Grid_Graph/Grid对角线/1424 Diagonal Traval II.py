'''
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

https://leetcode.com/problems/diagonal-traverse-ii/
'''


# 对角线 traversal的秘诀在于找到 对应遍历的规律, (i, j), 正反对应的idx
# 例如 0 对应 -n, n -1 对应 -1


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        minIdx, maxIdx = math.inf, -math.inf
        
        mapping = collections.defaultdict(deque)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                mapping[i + j].appendleft(nums[i][j])
                minIdx, maxIdx = min(minIdx, i + j), max(maxIdx, i + j)
        
        res = []
        # return [val for key in mapping for val in mapping[key]]
        for idx in range(minIdx, maxIdx + 1):
            res.extend(val for val in mapping[idx])
        
        return res




class Solution: # Same solution as above
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        
        mapping = collections.defaultdict(deque) # deque 方便appendleft
        for i in range(len(nums)):
            for j in range(len(nums[i])):  #这一步是处理了不规则的 grid(有残缺)
                mapping[i + j].appendleft(nums[i][j])
        
        return [val for key in mapping for val in mapping[key]]



#######---------------
#### Other directions:

# 从右上角忘右下角斜线：
mapping = collections.defaultdict(deque)
for i in range(len(nums)):
    for j in range(-len(nums[i]), 0, 1):
        mapping[abs(i - j)].appendleft(nums[i][j])

for i in range(5, 0, -1):
    print(i, list(mapping[i]))

# nums = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]

# 5 [7]
# 4 [8, 4]
# 3 [9, 5, 1]
# 2 [6, 2]
# 1 [3]
