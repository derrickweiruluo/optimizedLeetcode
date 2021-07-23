class Solution:
    def numTrees(self, n: int) -> int:
        
        # DP Buttom up approach
#         dp = [0] * (n + 1)
#         dp[0] = 1
#         dp[1] = 1
        
#         for i in range(2, n + 1):
#             for case in range(i):
#                 dp[i] += dp[case] * dp[i - 1 - case]
                
#         return dp[n]
        
        res = count = 1
        
        for i in range(1, n + 1):
            res = res * (i + n) // i
            count += 1
        
        return res // count
