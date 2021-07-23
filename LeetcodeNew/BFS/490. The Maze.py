class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        queue = collections.deque([start])
        rows, cols = len(maze), len(maze[0])
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        while queue:
            x, y = queue.popleft()
            # Both the ball and the destination exist in an empty space, 
            # and they will not be in the same position initially
            if x == destination[0] and y == destination[1]:
                return True
            
            for dx, dy in dirs:
                xi, yi = x + dx, y + dy
                while 0 <= xi < rows and 0 <= yi < cols and maze[xi][yi] == 0:
                    xi, yi = xi + dx, yi + dy
                xi, yi = xi - dx, yi - dy
                # 这是走到尽头前的前一步，by BFS
                if (xi, yi) not in visited:
                    visited.add((xi, yi))
                    queue.append((xi, yi))
                    
        return False
