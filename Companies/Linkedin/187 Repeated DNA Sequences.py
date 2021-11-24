'''
给一个string DNA序列，找出 10-letter long 的重复序列

'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        visited = set()
        res = set()
        if len(s) < 10: return []
        for i in range(len(s) - 9):
            print(i)
            cur = str(s[i : i + 10])
            if cur in visited:
                res.add(cur)
            else:
                visited.add(cur)
        
        return list(res)