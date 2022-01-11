'''
加减乘除括号
'+', '-', '*', '/' operators, and open '(' and closing parentheses ')'
'''


# https://leetcode.com/problems/basic-calculator-iii/discuss/127881/Python-O(n)-Solution-using-recursion

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        num = 0
        for i, char in enumerate(s + '+'):
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '(':
                stack.append(sign)
                stack.append('(')
                sign = '+'
            elif char in '+-*/)':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                elif sign == '*':
                    stack.append(int(stack.pop() * num))
                
                if char == ')':
                    num, item = 0, stack.pop()
                    while item != '(':
                        num += item
                        item = stack.pop()
                    sign = stack.pop()
                else:
                    sign, num = char, 0
            
        return sum(stack)

s = 2*(5+5*2)/3