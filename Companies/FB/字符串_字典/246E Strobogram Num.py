'''
Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false

'''


# Clarifications: any leading zeros or non-valid numnber?

class Solution: #BEST
    def isStrobogrammatic(self, num: str) -> bool:
        
        matching = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        
        i,j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in matching:
                return False
            i += 1
            j -= 1
        return True
        

class Solution:  # Similar, but not the best
    def isStrobogrammatic(self, num: str) -> bool:
        reverse = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}
        res = []
        
        for digit in num:
            if digit not in reverse:
                return False
            res.append(reverse[digit])
        
        res = ''.join(res[::-1])
        
        return res == num