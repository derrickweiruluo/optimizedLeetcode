## ******. Monotonous increase stack. *****. 

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_index = {}
        
        # 构建 Monotonous increase stack
        for idx, char in enumerate(s):
            last_index[char] = idx
        
        res = []
        
        for idx, char in enumerate(s):
            if char not in res:
                
                # res[-1] is a char that has an index MUST < than current idx
                # cond1: res 非空
                # cond2: idx < last_index[res[-1]] means res[-1] can be pop 因为dict里面还有
                # cond3: char < res[-1] lexicographically
                    
                while res and idx < last_index[res[-1]] and char < res[-1]:
                    res.pop()
                res.append(char)
        
        return ''.join(res)
