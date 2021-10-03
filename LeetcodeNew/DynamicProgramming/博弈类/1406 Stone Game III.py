'''
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.

https://leetcode.com/problems/stone-game-iii/discuss/564260/JavaC%2B%2BPython-DP-O(1)-Space
'''
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        memo = {}  # memo of {idx: score diff}
        n = len(stoneValue)
        score = self.dfs(0, stoneValue, memo, n)
        if score > 0: return 'Alice'
        elif score == 0: return 'Tie'
        else: return 'Bob'
        
    def dfs(self, idx, nums, memo, n):
        if idx in memo:
            return memo[idx]
        if idx >= n:
            return 0
        
        res = -math.inf
        preSum = 0
        for x in range(1, 4):
            if idx + x - 1 >= n:
                break
            preSum += nums[idx + x - 1]
            # my_best_margin_score == preSum - opponent's next max move
            res = max(res, preSum - self.dfs(idx + x, nums, memo, n))
        memo[idx] = res
        return memo[idx]
    