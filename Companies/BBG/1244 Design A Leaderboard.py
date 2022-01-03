'''
Design a Leaderboard class, which has 3 functions:

1.  addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
2.  top(K): Return the score sum of the top K players.
3.  reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
'''

class Leaderboard:
    # O(1), O(1), top O(NlogK), reset O(1), space O(n)
    def __init__(self):  
        self.score_board = collections.defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.score_board[playerId] += score

    def top(self, K: int) -> int:
        # print(self.score_board)
        lst_val = list(self.score_board.values())
        lst_val.sort()
        # print(lst_val)
        return sum(lst_val[:-(K + 1):-1])

    def reset(self, playerId: int) -> None:
        self.score_board[playerId] = 0



#*--------------

class Leaderboard:

    def __init__(self):
        self.counter = collections.Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.counter[playerId] += score

    def top(self, K: int) -> int:
        return sum(score for playerId, score in self.counter.most_common(K))

    def reset(self, playerId: int) -> None:
        self.counter[playerId] = 0

