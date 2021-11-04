'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = collections.defaultdict(int)
        memo = {}
        memo[0], memo[1], memo[2] = 0, 1, 2
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]
            