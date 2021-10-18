'''
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

'''

class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(char)
                res = max(res, len(stack))
            elif char == ')':
                stack.pop()
        
        return res

class SolutionLee:  # O(1)
    def maxDepth(self, s):
        res = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                res = max(res, cur)
            if c == ')':
                cur -= 1
        return res