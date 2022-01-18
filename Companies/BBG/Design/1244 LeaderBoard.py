'''
1.  addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
2.  top(K): Return the score sum of the top K players.
3.  reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.



'''
# Clarifications:
# Initially, the leaderboard is empty.
# It's guaranteed that K is less than or equal to the current number of players.
class Node(object):
    def __init__(self, score):
        self.score = score
        self.prev = None
        self.next = None

class Leaderboard(object):

    def __init__(self):
        self.players = {}
        self.head = Node(-float('inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):  #O(1)
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert(self, node):  # O(N)
        tail = self.tail
        while tail.score > node.score:
            tail = tail.prev
        tail.next.prev = node
        node.prev = tail
        node.next, tail.next = tail.next, node
    
    def addScore(self, playerId, score):  #O(N)
        if playerId in self.players:
            node = self.players[playerId]
            node.score += score
            self._remove(node)
        else:
            node = Node(score)
            self.players[playerId] = node
        self._insert(node)

    def top(self, K):  # O(K)
        # Top K players with most scores
        # # Top K players with most scores
        res = 0
        k = 0
        p = self.tail.prev
        while k < K and p != self.head:
            res += p.score
            p = p.prev
            k += 1
        return res
    
    def reset(self, playerId):  # O(1)
        node = self.players[playerId]
        self._remove(node)
        del self.players[playerId]



# Top NlogK 解法，by sorting
class Leaderboard:

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