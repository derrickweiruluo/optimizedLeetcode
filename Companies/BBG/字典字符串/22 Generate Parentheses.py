'''
给一个 n， generate all possible valid parenthese combination
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(left, right, subString):
            if left == 0 and right == 0:
                res.append(subString)
                return
            if left > 0:
                dfs(left - 1, right, subString + "(")
            if right > left:
                dfs(left, right - 1, subString + ")")
        
        dfs(n, n, '')
        return res
    
#   1 <= n <= 8


# iterative
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        comp_list = [['']]
        
        for i in range(1,n+1):
            res = []
            
            for j in range(i):
                for left in comp_list[i-1-j]:
                    for right in comp_list[j]:
                        res.append( '(' + left + ')' + right)
                        
            comp_list.append(res)

        return comp_list[-1]