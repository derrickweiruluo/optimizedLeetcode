'''
The idea is to use bruteforce: simulate our process and check all possibilities, but do it carefully.

First we need to choose direction where each figure will move, it is kept in dirs tuple of pairs.
Also we have stopped_mask variable, which is to understand if we stopped or not. For example 101 mask will mean that we stopped on the second figure and did not stop on first and third.
When we do one step, we need to decide where we continue and where we are not. For example if we have mask 101, then we have 4 options: we can continue move for first and third figure, we can stop on one of them or stop on both.
Also we need to deal with cases when two figures are on the same place and that we did not reach out of board.
Complexity
Time complexity is O(29^4) for the case of 4 queens, space complexity is O(1).


'''

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        self.directions = {
            "rook": [(-1, 0), (1, 0), (0, -1), (0, 1)],
            "bishop": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
            "queen": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        }

        self.n = len(pieces)
        self.ans = set()
        self.dirs = [0] * self.n

        def setDirections(cur):
            if cur == self.n:
                pos = [(positions[i][0], positions[i][1]) for i in range(self.n)]
                dfs(pos, 0)
                return

            for i in range(len(self.directions[pieces[cur]])):
                self.dirs[cur] = self.directions[pieces[cur]][i]
                setDirections(cur + 1)

        def dfs(pos, stopped):
            self.ans.add(tuple(pos))

            if stopped == (1 << self.n) - 1:
                return

            for mask in range(1 << self.n):
                if stopped & mask: continue

                visit = set()
                new_pos = []
                new_stopped = stopped ^ mask

                for i in range(self.n):
                    nr, nc = pos[i][0], pos[i][1]

                    if not (new_stopped & (1 << i)):
                        nr += self.dirs[i][0]
                        nc += self.dirs[i][1]

                    if 1 <= nr < 9 and 1 <= nc < 9 and (nr, nc) not in visit:
                        new_pos.append((nr, nc))
                        visit.add((nr, nc))

                if len(new_pos) == self.n:
                    dfs(new_pos, new_stopped)

        setDirections(0)

        return len(self.ans)