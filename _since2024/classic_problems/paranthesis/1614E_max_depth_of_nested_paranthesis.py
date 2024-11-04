"""
Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3

Example 3:
Input: s = "()(())((()()))"
Output: 3
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        left = 0
        for i, char in enumerate(s):
            if char == "(":
                left += 1
                res = max(res, left)
            elif char == ")":
                left -= 1
        return res
