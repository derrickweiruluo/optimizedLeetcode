'''
Start at 1, k == 2
[1,2,3,4,5],    start at 1, next are 2, 3
[1,_,3,4,5],    start at 3, next are 4, 5
[1,_,3,_,5],    start at 5, next are 5, 1
[_,_,3,_,5],    start at 3, next are 3, 5
[_,_,3,_,_]
'''

# In the end,n = 1,
# the index of winner index is 0 (base-0)

# We think with one step back,
# when n = 2,
# the index of winner is 0 + k,
# but we have only n peopple,
# so the winner index is (0 + k) % 2 (base-0)

# We think with one more step back,
# when n = 3,
# the index of winner is f(2) + k,
# but we have only n peopple,
# so the winner index is (f(2) + k) % 3 (base-0)

# We think with n more step back,
# the index of winner is f(n-1) + k,
# but we have only n peopple,
# so the winner index is (f(n-1) + k) % n (base-0)


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        winner = 0 # think the problem backward, from the last winner
        
        for i in range(1, n + 1):
            winner = (winner + k) % i
        
        return winner + 1


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        winner = 0 # think the problem backward, from the last winner
        start = 0
        
        for i in range(1, n + 1):
            winner = (winner + k) % i
        
        winner = winner + 1 + start
        return (winner) % n if winner > n else winner