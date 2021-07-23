class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
#     *** DFS TLE ***
#         for i in range(len(rooms)):
#             for j in range(len(rooms[0])):
#                 if rooms[i][j] == 0:
#                     self.dfs(rooms, i, j, 0)
        
#     def dfs(self, rooms, i, j, dist):
#         for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#             if 0 <= i + dx < len(rooms) and 0 <= j + dy < len(rooms[0]) and rooms[i + dx][j + dy] > rooms[i][j] :
#                 rooms[i + dx][j + dy] = dist + 1
        
#                 self.dfs(rooms, i + dx, j + dy, dist + 1)

        queue = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < len(rooms) and 0 <= y + dy < len(rooms[0]) and rooms[x + dx][y + dy] > rooms[x][y]:
                    rooms[x + dx][y + dy] = rooms[x][y] + 1
                    queue.append((x + dx, y + dy))
