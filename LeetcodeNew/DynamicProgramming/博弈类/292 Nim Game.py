'''
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
'''



class Solution:
    def canWinNim(self, n: int) -> bool:
        
        # Math
        return n % 4 in (1,2,3)
        
        
        # DP  --> TLE
        
        dp = [False] * max(n + 1, 4)  # player start from idx 0
        dp[1] = dp[2] = dp[3] = True
        
        # 前四个石头，先手[T, F, F, F], initialize the DP with this info
        # If dp[i] want to win the game, it MUST at least one of dp[i -1] dp[i -2] dp[i - 3] fail
        # dp[i] will be the a sure condition as we move on
        
        for i in range(4, n + 1):
            dp[i] = not dp[i - 1] or not dp[i - 2] or not dp[i - 3]
        
        return dp[n]