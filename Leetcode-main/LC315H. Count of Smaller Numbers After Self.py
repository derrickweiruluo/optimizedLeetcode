class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: index + 1 for index, val in enumerate(sorted(nums))} #先把数组从小到大排列，并且从1到n标记 {数：位置}
        n = len(nums)
        res = []
        BITree = [0] * (n + 1) #全是0的BIT， len是n+1
        
        def update(index):
            while (index <= n):
                BITree[index] += 1
                index += index & -index
                
        def presum(index):
            result = 0
            while index >= 1:
                result += BITree[index]
                index -= index & -index
            return result
        
        for num in reversed(nums): #不懂为什么要反转
            res.append(presum(rank[num] - 1))
            update(rank[num])
        return res[::-1]
