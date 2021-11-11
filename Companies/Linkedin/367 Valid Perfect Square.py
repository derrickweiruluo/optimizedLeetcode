'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1: return True
        if num < 4: return False
        
        left, right = 1, num // 2
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 < num:
                left = mid + 1
            else:
                right = mid
        
        return left ** 2 == num