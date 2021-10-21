'''
Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Garentee to be a valid input

'''

class Solution:
    def calculate(self, s: str) -> int:
        
        prev = 0
        cur = 0
        stack = []
        sign = 1
        # initialy, prev, sign is default at 0 and 1
        
        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char in '-+':
                prev += cur * sign  # close a local calculation, 
                sign = 1 if char == '+' else -1
                cur = 0             # restart
            elif char == '(':
                stack.append(prev)
                stack.append(sign)
                prev, sign = 0, 1   # restart
            elif char == ')':
                prev += cur * sign  # close a local (inner) calculation
                prev *= stack.pop()
                prev += stack.pop()
                cur = 0             # restart
        
        return prev + sign * cur