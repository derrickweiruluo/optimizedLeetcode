'''
给一段 Valid 的字符串，返回他的括号最深深度


s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
'''
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/discuss/888949/JavaC%2B%2BPython-Parentheses-Problem-Foundation
class Solution:
    def maxDepth(self, s: str) -> int:
        
        # O(n), O(1) space 
        res = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                res = max(res, cur)
            elif c == ')':
                cur -= 1
        return res
        
        
class Solution: # O(N) for both, NOT GOOD
    def maxDepth(self, s: str) -> int:   
        # *---------
        res = 0
        stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(char)
                res = max(res, len(stack))
            elif char == ')':
                stack.pop()
        
        return res