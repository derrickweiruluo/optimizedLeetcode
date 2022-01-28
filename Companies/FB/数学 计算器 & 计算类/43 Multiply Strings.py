'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''



# Clarifications:
# num1 and num2 consist of digits only. --> 正整数
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # corner cases, either num1 or num2 == 0 will return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == '1': return num2
        if num2 == '1': return num1
        
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        
        # nested for loop for indexing every digit and update res[i + j] and res[i + j + 1] accordingly
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                res[i + j + 1] += int(num1[i]) * int(num2[j])
                res[i + j] += res[i + j + 1] // 10
                res[i + j + 1] %= 10
                
        
        # remove and leading 0 in the res[]
        return "".join(map(str, res)).lstrip("0")