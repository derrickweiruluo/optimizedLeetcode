class Solution:
    def pathSum(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for num in nums: #建立一个 {层-位}：val的dict
            depth = num // 100
            pos = (num - depth * 100) // 10
            val = num % 10
            dict[depth, pos] += dict[depth - 1, (pos + 1) // 2] + val
            
        res = 0
        for depth,pos in dict.keys():
            # 查询当前节点下面在不在dict里面
            if (depth+1, pos*2-1) not in dict and (depth+1,pos*2) not in dict:
                res += dict[depth,pos]
        return res
