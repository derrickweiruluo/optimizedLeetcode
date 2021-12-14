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
class Solution: # O(1) space 
    def removeDuplicates(self, s: str) -> str:
        
        # O(1) space, one pass
        s = list(s)
        i = 0
        
        for j in range(len(s)):
            # 利用 i pointer 作为 一个stack， modified and rearrange s[:i]
            # i += 1, -= 1 as appending/popping to stack
            if i == 0:              # as if stack if empty
                s[i] = s[j]
                i += 1
            else:
                char1, char2 = s[i - 1], s[j]
                if char1 == char2:  # find matching stack[-1] to cur
                    i -= 1          # stack.pop()
                else:
                    s[i] = s[j]     # append to stack
                    i += 1          # advance the stack idx
            
        
        return "".join(s[:i])



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