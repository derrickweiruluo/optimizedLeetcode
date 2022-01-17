'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
'''


# clarification: 
# Roman numerals are usually written largest to smallest from left to right.

class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        
        res, prev = 0, 0
        # Roman numerals are usually written largest to smallest from left to right.
        # that is why when go backward, + first and - later if applicable

        for char in s[::-1]:
            if mapping[char] >= prev:
                res += mapping[char]
            else:
                res -= mapping[char]
            prev = mapping[char]
        
        return res




class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        
        res = 0
        for i, char in enumerate(s):
            add = mapping[char]
            res += add
            if i > 0 and s[i-1: i+1] in mapping:
                res -= (mapping[s[i]] + mapping[s[i - 1]])
                res += mapping[s[i-1: i+1]]
        return res
            