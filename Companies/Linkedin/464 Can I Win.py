'''
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.



# Draw card without replacement
# both play optimally
'''

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # just cleanner codes this time
        def canWin(choices, rem):
            cur = str(choices)
            if choices[-1] >= rem:
                seen[cur] = True
                return seen[cur]
            if cur in seen:
                return seen[cur]
            for i in range(len(choices)):
                if not canWin(choices[:i] + choices[i + 1:], rem - choices[i]):
                    seen[cur] = True
                    return seen[cur]
            seen[cur] = False
            return seen[cur]
            
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        choices = list(x for x in range(1, maxChoosableInteger + 1))
        seen = {}
        return canWin(choices, desiredTotal)