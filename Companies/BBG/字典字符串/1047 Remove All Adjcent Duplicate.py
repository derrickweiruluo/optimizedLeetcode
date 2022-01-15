class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Anonther O(N) + O(1) solution
        s = list(s)
        i = 0
        
        for j in range(len(s)):
            # 利用 i pointer 作为 一个stack， modified and rearrange s[:i]
            # i 是 stack 外的bound, stack[:i] 里面是stack的内容
            # i += 1, -= 1 as appending/popping to stack
            if i > 0 and s[i - 1] == s[j]:             #if stack and stack[-1] match cur
                i -= 1
            else:
                s[i] = s[j]          # advance the i pointer (append to stack)
                i += 1       
            
        
        return "".join(s[:i])
        
#* -----------------------------
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        # O(1) space, one pass
        s = list(s)
        i = 0
        
        for j in range(len(s)):
            # 利用 i pointer 作为 一个stack， modified and rearrange s[:i]
            # i += 1, -= 1 as appending/popping to stack
            if i == 0:              # as if stack if empty
                s[i] = s[j]         # advance the i pointer
                i += 1
            else:
                if s[i - 1] == s[j]:  # find matching stack[-1] to cur
                    i -= 1          # stack.pop()
                else:
                    s[i] = s[j]     # advance the i pointer (append to stack)
                    i += 1       
            
        
        return "".join(s[:i])