'''
The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
'''


# Clarifications:

# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.


class Solution: # O(1) 解法
    def scoreOfParentheses(self, s: str) -> int:
        
        res = depth = 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
            if char == ')' and s[i - 1] == '(':
                res += 2 ** depth
        return res
        