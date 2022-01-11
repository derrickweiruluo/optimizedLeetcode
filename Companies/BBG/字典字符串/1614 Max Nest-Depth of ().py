'''
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3, @ num 8
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Input: s = "(1)+((2))+(((3)))"
Output: 3, @ num 3

'''

class Solution:
    def maxDepth(self, s: str) -> int:
        
        res = 0
        left = 0
        for i, char in enumerate(s):
            if char == '(':
                left += 1
                res = max(res, left)
            elif char == ')':
                left -= 1
        
        return res