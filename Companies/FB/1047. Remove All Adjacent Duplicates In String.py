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
        
        s = list(s)
        
        slow = fast = 0
        
        while fast < len(s):
            if slow == 0:  # similar to stack is empty
                s[slow] = s[fast]
                slow += 1
            else:
                char1, char2 = s[slow - 1], s[fast]
                if char1 == char2:  # similar to stack[-1] == cur
                    slow -= 1
                else:               
                    s[slow] = s[fast]
                    slow += 1
            fast += 1
        
        return "".join(s[:slow])



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