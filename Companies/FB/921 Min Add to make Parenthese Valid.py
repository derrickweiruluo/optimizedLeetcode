'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''
        Intuition:  To make a string valid,
        we can add some '(' on the left,
        and add some ')' on the right.
        We need to find the number of each.
        
        Loop char c in the string S:
        if c == '(', we increment right,
        if c == ')', we decrement right.
        When right is already 0, we increment left, Return left + right in the end
        '''
        left = right = 0
        for char in s:
            if char == '(':
                right += 1
            else:
                if right:
                    right -= 1
                else:
                    left += 1
        return left + right