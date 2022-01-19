'''
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
'''

# Time complexity: O(2^n)
# Space complexity: O(k + n)
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


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]