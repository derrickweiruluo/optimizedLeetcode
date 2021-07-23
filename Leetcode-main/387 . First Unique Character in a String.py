class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapping = {}
        
        for i, val in enumerate(s):
            mapping[val] = mapping.get(val, []) + [i]
            
        
        # print(list(mapping.items()))
        
        res = len(s)
        
        for char, lst in mapping.items():
            if len(lst) == 1:
                return mapping[char][0]
        
        return -1
