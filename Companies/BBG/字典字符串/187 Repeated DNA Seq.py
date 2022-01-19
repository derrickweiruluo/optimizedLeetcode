'''
给一个string DNA序列，找出 10-letter long 的重复序列

'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n = len(s)
        if n < 10: return []
        
        visited = set()
        res = set()
        
        for i in range(len(s) - 9):
            cur = s[i: i + 10]
            if cur not in visited:
                visited.add(cur)
            else:
                res.add(cur)
        
        return list(res)