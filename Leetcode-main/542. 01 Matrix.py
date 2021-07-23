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
