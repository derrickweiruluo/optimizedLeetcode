'''
两个正数as string 相加，返回string

num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

'''


class Solution: # BEST, O(1) Space
    def addStrings(self, num1: str, num2: str) -> str:
        
        def convert(char):
            return ord(char) - ord('0')
        
        x1 = x2 = 0
        for num in num1:
            x1 = x1 * 10 + convert(num)
        for num in num2:
            x2 = x2 * 10 + convert(num)
        
        
        # clarification: whether I can convert int to str 
        return str(x1 + x2)
        
        
        
class Solution: 
    # Time: O(M+N), 
    # Space: Extra Space (without counting output as space): O(1)
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = []
        p1, p2 = len(num1) - 1, len(num2) - 1
        
        while p1 >= 0 or p2 >= 0 or carry:
            if p1 >= 0:
                carry += int(num1[p1])
                p1 -= 1
            if p2 >= 0:
                carry += int(num2[p2])
                p2 -= 1
            
            res.append(str(carry % 10))
            carry = carry // 10
        
        return ''.join(res[::-1])