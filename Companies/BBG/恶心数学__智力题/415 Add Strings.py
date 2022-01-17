'''
Input: num1 = "11", num2 = "123"
Output: "134"

Input: num1 = "456", num2 = "77"
Output: "533"

'''
class Solution:
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