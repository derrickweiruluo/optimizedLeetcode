'''
###  只包含加减括号


###  Contraints
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
'''

class Solution:
    def calculate(self, s: str) -> int:
        
        prev = 0
        cur = 0
        stack = []
        sign = 1
        # initialy, prev, sign is default at 0 and 1
        
        # every iteration, when char != digit, cur = 0
        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char in '-+':
                prev += cur * sign  # close the left calculation, 
                sign = 1 if char == '+' else -1
                cur = 0             # restart
            elif char == '(':
                stack.append(prev)
                stack.append(sign)
                cur = prev = 0   # restart the same at beginning
                sign = 1         # restart the same at beginning
            elif char == ')':
                prev += cur * sign      # close a local inner calculation
                prev *= stack.pop()     # right * sign, sign from stack
                prev += stack.pop()     # left + right, left from stack
                cur = 0
        
        return prev + sign * cur