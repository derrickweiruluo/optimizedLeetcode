'''
Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.


The integer division should truncate toward zero.
'''

s1 = "3+2*2"
s2 = " 3/2 "
s3 = " 3+5 / 2 "


def calculate(s):
    stack = []
    cur = 0
    sign = '+'

    for i, char in enumerate(s):
        if char.isdigit():
            cur = cur * 10 + int(char)
        elif char in '+-*/' or i == len(s) - 1:
            if sign == '+':
                stack.append(cur)
            elif sign == '-':
                stack.append(-1 * cur)
            elif sign == '*':
                stack.append(stack.pop() * cur)
            elif sign == '/':
                stack.append(int(stack.pop() / cur))
            cur = 0
            sign = char
    print(stack)
    return sum(stack)

# 3
# +, [3]
# 2, [3]
# * , [3 * 2]
print(calculate(s1))
print(calculate(s2))
print(calculate(s3))

