"""
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

####Constraints
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.
 
"""

def getFood(self, grid: List[List[str]]) -> int:
        
        # dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = collections.deque()
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    queue.append((i, j, 0))
                    
        
        while queue:  # one style
            print(len(queue))
            for i in range(len(queue)):
                x, y, dist = queue.popleft()
                # print(x, y)
                if grid[x][y] == '#':
                    return dist
                    # print(dist)
                for dx, dy in dirs:
                    xi, yi = x + dx, y + dy
                    if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]):
                        if grid[xi][yi] == 'O':
                            queue.append((xi, yi, dist + 1))
                            grid[xi][yi] = 'X'
                        elif grid[xi][yi] == '#':
                            return dist + 1
                            # queue.append((xi, yi, dist + 1))
                            
                            
        while queue: # stype two
            cur_step += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # print(x, y)
                for dx, dy in dirs:
                    xi, yi = x + dx, y + dy
                    if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]) and grid[xi][yi] != 'X':
                        if grid[xi][yi] == '#':
                            return cur_step
                        elif grid[xi][yi] == 'O':
                            grid[xi][yi] = 'X'
                            queue.append((xi, yi))


        return -1
