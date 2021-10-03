'''1025 Divisor Game
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

 

Ex1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Ex2:
Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
'''
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

'''
For N <= n, we have find that:
If N is even, can win.
If N is odd, will lose.

For the case N = n + 1
If N is even, we can win choosing x = 1,
give the opponent an odd number N - 1 = n,
force him to lose,
because we have found that all odd N <= n will lose.

If N is odd, there is no even x that N % x == 0.
As a result, we give the opponent a even number N - x,
and the opponent can win,
because we have found that all even N <= n can win.

Now we prove that, for all N <= n,
If N is even, can win.
If N is odd, will lose.
'''