'''
Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
'''

#
class Solution: # Interview
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


class Solution: #  Interview::  Time O(N), Space O(1)
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
                char1, char2 = s[i - 1], s[j]
                if char1 == char2:  # find matching stack[-1] to cur
                    i -= 1          # stack.pop()
                else:
                    s[i] = s[j]     # advance the i pointer (append to stack)
                    i += 1          
            
        
        return "".join(s[:i])


''' Follow-up: if remove deplicates within a len of k
'''
class Solution:  # FOLLOW-UP ONLY
    def removeDuplicates(self, s: str) -> str:
        stack = [] # stack of (char, its cnt)
        for num in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            elif stack[-1][1] < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        
        return ''.join(char * cnt for char, cnt in stack)








# O(N) and O(N - D), where D is the num of duplicates
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        res = []
        
        for char in s:
            if res and res[-1] == char:
                res.pop()
            else:
                res.append(char)
                
        return "".join(res)