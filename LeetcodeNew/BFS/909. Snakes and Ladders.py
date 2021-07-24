class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        moves = {1: 0}
        queue = collections.deque([1])
        N = len(board)
        
        while queue:
            pos = queue.popleft()
            if pos == N * N:
                return moves[pos]
            
            for next_pos in range(pos + 1, min(pos + 6, N * N) + 1):
                row, col = self.get_index(next_pos, N)
                if board[row][col] != -1:
                    next_pos = board[row][col]
                if next_pos not in moves:
                    moves[next_pos] = moves[pos] + 1
                    queue.append(next_pos)
        return -1
    
    def get_index(self, x, N):
        quotient, remainder = divmod(x - 1, N)
        row = N - quotient - 1
        if row % 2 == N % 2:
            col = N - 1 - remainder
        else:
            col = remainder
        
        return row, col
