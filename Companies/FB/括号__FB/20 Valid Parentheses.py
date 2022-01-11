'''
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        parDict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if stack and char == parDict[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False