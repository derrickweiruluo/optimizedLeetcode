


# Time O(M^2 * N^2), Space O(1)
# MN time to scan
# might keep crushing 3-candy, with all candies are gone


class Solution:
    def candyCrush(self, grid: List[List[int]]) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        
        
        while True:
        # 总 while loop来确认每一次的下降，当 step 1，2，3完成后
        # 下一次在重复相同的步骤 in the crushed board
        # until the crush set is empty

            #1 第一次下落
            crush = set()
            for i in range(m):
                for j in range(n):
                    # i, j 都 > 1 是因为预留两行两列
                    if j > 1 and grid[i][j] and grid[i][j] == grid[i][j - 1] == grid[i][j - 2]:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}
                    if i > 1 and grid[i][j] and grid[i][j] == grid[i - 1][j] == grid[i - 2][j]:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}
            
            # 2, Crush
            if not crush: break   # 跳出while loop条件
            for i, j in crush: 
                grid[i][j] = 0

            # 3, Drop
            for j in range(n):
                bottom = m - 1
                # dropping the candice and move up the bottome for the cur column
                for i in range(m - 1, -1, -1):
                    if grid[i][j]: 
                        grid[bottom][j] = grid[i][j]
                        bottom -= 1
                
                # update everything above the bottom line to zeroes
                for i in range(bottom + 1): 
                    grid[i][j] = 0
                    
        return grid



# 1D Candy Crush

def candy_crush(col):
    if not col:
        return col
    
    stack = []
    stack.append([col[0], 1])
    
    for i in range(1, len(col)):
        if col[i] != col[i-1]:
            if stack[-1][1] >= 3:
                stack.pop()
            if stack and stack[-1][0] == col[i]:
                stack[-1][1] += 1
            else:
                stack.append([col[i], 1])
        else:
            stack[-1][1] += 1
            
    # handle end
    if stack[-1][1] >= 3:
        stack.pop()
        
    out = []
    for ltrs in stack:
        out += ltrs[0] * ltrs[1]
    
    return ''.join(out)
    
print(candy_crush("aaaabbbc")) #c
print(candy_crush("aabbbacd")) #cd
print(candy_crush("aabbccddeeedcba")) #blank expected
print(candy_crush("aabbbaacd")) #cd
print(candy_crush("dddabbbbaccccaax")) #x