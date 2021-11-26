'''
一个奇怪的括号题

1. Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
2. Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
'''

class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        res represents the number of left/right parentheses already added.
        right represents the number of right parentheses needed.
        
        (1) case ')'
        If we meet a right parentheses , right--.
        If right < 0, we need to add a left parentheses before it.
        Then we update right += 2 and res++
        This part is easy and normal.

        (2) case '('
        If we meet a left parentheses,
        we check if we have odd number ')' before.
        If so, we add one ')' here, then update right--; res++;.
        Note that this part is not necessary if two consecutive right parenthesis not required.

        Because we have ), we update right += 2.
        
        Dry run
        All by @himanshusingh11:

        Example 1: Consider ((()(,n= 5 ,i=0,1...4
        '''
        res, right = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                right += 2
                if right % 2 == 1:
                    right -= 1
                    res += 1
            else:
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        
        return res + right
            
                
            
                