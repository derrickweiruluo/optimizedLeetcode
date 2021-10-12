'''
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down)

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false

Example 4:
Input: num = "1"
Output: true

'''

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        reverse = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}
        res = []
        
        for digit in num:
            if digit not in reverse:
                return False
            res.append(reverse[digit])
        
        res = ''.join(res[::-1])
        
        return res == num