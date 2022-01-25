'''
Given two binary strings a and b, return their sum as a binary string.

 
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

# Time O(max(m, n))
# Space  O(max(m, n)) for the output
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        res = ''
        a, b = list(a), list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res += str(carry % 2)
            carry = carry // 2
        
        return res[::-1]