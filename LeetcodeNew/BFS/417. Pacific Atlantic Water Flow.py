class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific_visited = set()
        atlantic_visited = set()
        
        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for direction in dirs:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if heights[next_i][next_j] >= heights[i][j]:
                        traverse(next_i, next_j, visited)
        
        
        # check the left right borders first:
        for i in range(rows):
            traverse(i, 0, pacific_visited)
            traverse(i, cols - 1, atlantic_visited)
        
        # check the up down borders first:
        for j in range(cols):
            traverse(0, j, pacific_visited)
            traverse(rows - 1, j, atlantic_visited)
        
        return list(pacific_visited & atlantic_visited)
