'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.



Constraints:  # Clarifiy with 面试官
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All intermediate results will be in the range of [-231, 231 - 1].
'''

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# Non-Negative
# The answer is guaranteed to fit in a 32-bit integer.

class Solution: # O(1) space
    def calculate(self, s: str) -> int:
        
        # O(1) space 解法
        prev, cur = 0, 0    # prev is lower level, cur is high level 
        prevSign = 1        # prevSign is for lower level operation with prev
        op, num = 0, 0      # op is for the high level operation with cur
        # op in [0, 1, -1], for "+-", "x","/" respectively  
        
        for i, char in enumerate(s):
            if char.isdigit(): # 所有运算都在这一步
                num = num * 10 + int(char)
                if i == len(s) - 1 or not s[i + 1].isdigit():
                    if op == 0: cur = num
                    if op == 1: cur *= num
                    if op == -1: cur = int(cur /num)
            
            elif char in "*/":
                op = 1 if char == '*' else -1
                num = 0
            
            elif char in "+-":  # reset back to default state (op, num, cur)
                prev += prevSign * cur
                prevSign = 1 if char == "+" else -1
                cur = num = op = 0
        
        # When at the end, the result of high-level become prev or cur
        return prev + prevSign * cur




class Solution:
    def calculate(self, s: str) -> int:
        preSign = '+'
        cur = 0
        stack = []  # stack to store prevNum at top of the stack
        
        for i, char in enumerate(s):
            if char.isdigit():
                cur = cur * 10 + int(char)
            
            # !!!! 下面的是 if，不是 elif，因为最后一位是数字的话，要额外运算
            if char in '+-*/' or i == len(s) - 1: # the previous operation
                if preSign == '+':
                    stack.append(cur)
                elif preSign == '-':
                    stack.append(-cur)
                elif preSign == '*':
                    stack.append(stack.pop() * cur)
                elif preSign == '/':
                    stack.append(int(stack.pop() / cur))
                cur = 0
                preSign = char
        #     print(char, stack) 
        # print(stack)    
        return sum(stack)
    
# s = "3+2*2"
# a = Solution()
# print(a.calculate(s))