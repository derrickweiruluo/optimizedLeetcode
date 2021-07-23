class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []
        last_seen = {}
        max_last_seen, count = 0, 0
        
        for i, char in enumerate(s):
            # 1. 记录每个char的最大index
            last_seen[char] = i
        
        for i, char in enumerate(s):
            # 2. 每一段都记录里面存在的 char 的last index(最大index)
            # 3. 一旦 index == last_seen[index], 可以切割，并reset长度
            max_last_seen = max(max_last_seen, last_seen[char])
            count += 1
            if i == max_last_seen:
                res.append(count)
                count = 0
        
        
        return res
      
 # https://leetcode.com/problems/partition-labels/
