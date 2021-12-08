'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

'''

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        sign = '+'  #画龙点睛
        
        for i, char in enumerate(s):
            if char.isdigit():
                cur = cur * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(cur)
                elif sign == '-':
                    stack.append(-cur)
                elif sign == '*':
                    stack.append(stack.pop() * cur)
                elif sign == '/':
                    stack.append(int(stack.pop() / cur))
                    # print(-3 //2)
                    # print(int(-3 /2))
                cur = 0
                sign = char
        
        # print(stack)    
        return sum(stack)
    
# s = "3+2*2+2*2+2"
# a = Solution()
# print(a.calculate(s))