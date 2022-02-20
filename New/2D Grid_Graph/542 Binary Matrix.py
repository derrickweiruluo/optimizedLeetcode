'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''

class Solution:  # 520 ms, faster than 96.50%
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):  # compute dist of top & left neighbor
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):  # conmpute the res based on bottom/right
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat







class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque()
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                # Adding the "0" to the set, which will never be visited
                if mat[i][j] == 0:
                    # print(i, j)
                    visited.add((i, j))
                    queue.append((i, j))
        
        print(queue)
        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                xi, yi = x + dx, y + dy
                # if xi, yi in range and not visited before, 
                if 0 <= xi < rows and 0 <= yi < cols and (xi, yi) not in visited:
                    # print(xi, yi)
                    # this step to update next un-visited pos = curr post + 1
                    mat[xi][yi] = mat[x][y] + 1
                    queue.append((xi, yi))
                    visited.add((xi, yi))
            # print(queue)
                  
        # NOTE: the above print statement helps to visualize the queue and visited actions
        return mat