'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
'''

# 每个character只能用一次
# 保留relative order
# mono-increasing stack

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_index = {}
        
        # 构建 {char : last appeared idx}
        for idx, char in enumerate(s):
            last_index[char] = idx
        
        res = []
        
        for idx, char in enumerate(s):
            if char not in res:
                
                # res[-1] is a char that has an index MUST < than current idx
                # cond1: res 非空
                # cond2: 当前char 比 res[-1] 小
                # cond3: 且res[-1] 对应的 char 后面还有重复的
                    
                while res and char < res[-1] and idx < last_index[res[-1]]:
                    res.pop()
                res.append(char)
        
        return ''.join(res)