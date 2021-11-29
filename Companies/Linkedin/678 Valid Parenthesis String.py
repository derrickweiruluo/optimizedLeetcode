'''
Given a string s containing only three types of characters: 
'(', ')' and '*', 

"*" can be treated as a magic char
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
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
        closingMax, closingMin = 0, 0
        for char in s:
            if char == '(':
                closingMax += 1
                closingMin += 1
            if char == "*":
                # '*' could be treated as a single right parenthesis ')' or 
                # a single left parenthesis '(' or an empty string "".
                closingMax += 1
                closingMin = max(closingMin - 1, 0)
            if char == ')':
                closingMax -= 1
                closingMin = max(closingMin - 1, 0)
            if closingMax < 0:
                return False
        
        return closingMin == 0