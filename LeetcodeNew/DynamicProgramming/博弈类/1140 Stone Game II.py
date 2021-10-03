'''
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.


Ex 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.  

https://docs.google.com/presentation/d/18czsiBAEk08ChqQPkg7uJ8ER8jmATmipASlzc8Ofp6A/edit#slide=id.g8cb2d0e32e_0_19
https://github.com/Taoge123/OptimizedLeetcode/blob/master/DailyChallenge/LC_1140.py
https://leetcode.com/problems/stone-game-ii/discuss/345230/JavaPython-DP-Solution

https://leetcode.com/submissions/detail/564240376/
'''

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = dict()  # memo of {(stone_taken, M_Value) : opt_score}
        n = len(piles)
        return self.dfs(0, 1, piles, memo, n)
    
    def dfs(self, taken, M, piles, memo, n):
        if (taken, M) in memo:              # memo of {(taken stones, M-Value) : res}
            return memo[(i, M)]
        if taken >= n:                      # 边界限制
            return 0
        if taken + 2 * M >= n:              # 后面都是对手的，剩余数量不足2M，对手通吃
            return sum(piles[taken:])
        res = 0
        for x in range(1, 2 * M + 1):   # player can take X piles, where 1 <= X <= 2M
            newM = max(M, x)
            # DFS 自己每一个可走的玩法，取最优值， 深度搜索 
            res = max(res, sum(piles[taken:]) - self.dfs(taken + x, newM, piles, memo, n))
            memo[(taken, M)] = res

        return memo[(taken, M)]