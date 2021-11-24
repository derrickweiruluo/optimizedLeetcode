'''
Given a string s containing only three types of characters: 
'(', ')' and '*', 

"*" can be treated as a magic char

return true if s is valid.

'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Explanation:
        We count the number of ')' we are waiting for,
        and it's equal to the number of open parenthesis.
        This number will be in a range and we count it as [cmin, cmax]

        cmax counts the maximum open parenthesis,
        which means the maximum number of unbalanced '(' that COULD be paired.
        cmin counts the minimum open parenthesis,
        which means the number of unbalanced '(' that MUST be paired.
        
        The string is valid for 2 condition:

        cmax will never be negative.
        cmin is 0 at the end
        '''
        closing_max, closing_min = 0, 0
        for i in s:
            if i == '(':
                closing_max += 1
                closing_min += 1
                
            if i == '*':
                closing_max += 1
                closing_min = max(closing_min - 1, 0)
                
            if i == ')':
                closing_max -= 1
                closing_min = max(closing_min - 1, 0)
                
            if closing_max < 0:
                return False
            
        return closing_min == 0