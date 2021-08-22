"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n

"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        src = image[sr][sc]
        
        def dfs(grid, i, j):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == newColor or grid[i][j] != src:
                return
            grid[i][j] = newColor
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
        
        dfs(image, sr, sc)
        
        return image
