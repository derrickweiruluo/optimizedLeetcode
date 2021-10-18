'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

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

'''

class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {"(" : ")", "[" : "]", "{" : "}"}
        # open_dict = {"(", "[", "{"}
        stack = []
        
        for i in s:
            if i in par_dict:
                stack.append(i)
            elif stack and i == par_dict[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []