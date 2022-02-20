"""
You are given an m x n grid rooms initialized with these three possible values.

    -1:     A wall or an obstacle.
    0:      A gate.
    INF:    Infinity means an empty room. 


Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF
"""



# Constraints:
# rooms[i][j] is -1, 0, or 231 - 1.


class Solution: #FAST, BFS with pruning
    def wallsAndGates(self, rooms):
        if not rooms:
            return 
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n= len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:   
                    #FAST, BFS with pruning
                    # 因为第一个门 BFS 过后, 会大大减少其它门的搜索
                    queue = collections.deque([(i + dx, j + dy, 1) for dx, dy in dirs])
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= m or y < 0 or y >= n or rooms[x][y] <= val:
                            continue
                        rooms[x][y] = val
                        for dx, dy in dirs:
                            queue.append((x + dx, y + dy, val+1))


# Below is extremely slow
class Solution:  # both O(mn)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # deque of all the gate
        queue = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            # 从每个gate的搜索，探索完可被探索的下一步就加进queue
            x, y = queue.popleft()
            for dx, dy in dirs:
                xi, yi = x + dx, y + dy
                # 下一层BFS符合条件有俩： 
                # 1. 下条路没开发过, 题意：INF Infinity means an empty room & distance to a gate is less than INF
                # 2. 下条路被开发过，但是当前距离门不是最优解
                # 3. 隐藏条件，wall是 -1，意味着wall不会被开发，，无法被BFS
                if 0 <= xi < len(rooms) and 0 <= yi < len(rooms[0]) and rooms[xi][yi] > rooms[x][y]:
                    rooms[xi][yi] = rooms[x][y] + 1
                    queue.append((xi, yi))
        
        
