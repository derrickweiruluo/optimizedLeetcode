'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        matching = {'(': ')', '[': ']', '{': '}'}
        stack = []
        
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or matching[stack.pop()] != char:
                    return False
        
        return not stack