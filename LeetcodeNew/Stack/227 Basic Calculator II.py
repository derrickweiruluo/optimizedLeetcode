'''
只有加减乘除的计算器

'''

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
                    print(-3 //2)
                    print(int(-3 /2))
                cur = 0
                sign = char
        print(stack)    
        return sum(stack)



class Solution:  # 05/2021
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        presign = '+'  #画龙点睛
        
        for cur in s + '+':   # 情况一，画龙点睛在数组后面加一个'+'来终结最后的运算
            if cur.isdigit():
                num = num * 10 + int(cur)
            elif cur in '-+*/':  #情况二
                if presign == '+':
                    stack.append(num)
                elif presign == '-':
                    stack.append(-num)
                elif presign == '*':
                    stack.append(num * stack.pop())
                elif presign == '/':
                    stack.append(math.trunc(stack.pop() / num)) #画龙点睛 math.trunc最直接粗暴，负数会导致向右边升一位

                presign = cur #reset 前置符号到当前
                num = 0 #当出现符号时，reset当前数为0
        
        return sum(stack)