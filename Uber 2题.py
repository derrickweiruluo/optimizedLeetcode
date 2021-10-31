'''
D1:
https://www.1point3acres.com/bbs/thread-807271-1-1.html
jump in an array, 比如给你一个array = [1, 2, 3, 1, 2, 3, 2, 1], 再给你一个diff = 2
每次jump都只能jump到同一个数字上面，而且两次jump的距离必须大于diff，返回最大可以jump的次数。

我上面给的例子，比如我决定jump number是1，那么就可以从第一个1跳到第二个一，距离是3 > diff, 所以这次jump是valid，从第二个跳到第三个1，距离是4，valid， 所以如果选择跳1的话，可以跳2次。

同理，选择‍‌‌‌‌‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌跳2，从第一个2可以跳到第二个2， 但是从第二个2跳到第三个时，距离只有2，不valid，所以只能跳一次。3也只能跳一次。所以上面的例子返回2.

Sol:
array存放到一个dict = {val, list of idx}, key是array里面的value，value是index的list，如果是valid的jump，就add这个index到list里面，最后拿到长度最长的list，返回list的长度
'''




'''
B2:
第二题是这个帖子里面的第二题 https://www.1point3acres.com/bbs/thread-799461-1-1.html String s = "abcdefghij", int[] size = {3,2,2,2,1}; 交换"abc"和"de",再交换"fg"和"hi", 最后剩下的那个不用换返回"deabchifgj". 上面pdf有类似的题
'''
s = 'abcdefghij'
s = 'codesignal'
size =  [4,3,1,1,1] #[3,2,2,2,1]
arr = []
for l in size:
    arr.append(s[:l])
    s = s[l:]
print(arr)
res = ''
for i in range(len(arr)):
    if i % 2 == 0:
        if i != len(arr) - 1:
            res += (arr[i + 1])
            res += (arr[i])
        else:
            res += (arr[i])
print(res)


'''     C3
消消乐点气球，如果这个点周围（上下左右）有>=2个bubble跟它颜色一样，就消掉，否则不消。消掉后value变成0，上面的bubble会落下来。返回最终bubbles的状态。
'''
ops = [(2,1)]
grid = [
[2,3,4,4],
[2,1,3,4],
[1,1,1,2],
[2,1,3,4]]
print(grid)
m, n = len(grid), len(grid[0])
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def fall(grid):
    for j in range(n):
        cur = [grid[r][j] for r in range(m - 1, -1, -1)]
        # print('the col before is: ', cur)
        if 0 not in cur: continue
        left, right = 0, 0
        while cur[left] != 0: left += 1
        right = left
        while cur[right] == 0: right += 1
        cur = cur[:left] + cur[right:] + cur[left:right]
        # print('the col after is: ', cur)
        for i in range(m):
            grid[i][j] = cur[-1 - i]
    return grid

for i, j in ops:
    color = grid[i][j]
    pos = []
    for dir in dirs:
        x = i + dir[0]
        y = j + dir[1]
        if 0 <= x < m and 0 <= y < n and grid[x][y] == color:
            pos.append((x, y))
        if len(pos) >= 2:
            grid[i][j] = 0
            for (x, y) in pos:
                grid[x][y] = 0
    grid = fall(grid)
print(grid) 
            

'''
D5
https://www.1point3acres.com/bbs/thread-761679-1-1.html
Leetcode 1743, DFS, 构建adj graph
'''
     

''' C6
3. 给一个 n x n 的矩阵，然后让你把一圈圈的数值按从小到大排列。
例如 matrix = [-1, 3, 5, 6, 7]     第一圈就是最外围数组成的 [-1, 3, 5, 6, 7, 2, 3, 1, 2, 5, 4, 3, 12, 1, -3, -2]
              [-2, 3, 4, 5, 2]     第二圈就是第二外围数组成的 [3, 4, 5, 2, 9, 14, 3, 9]
              [-3, 9, 1, 2, 3]     第五圈就是矩阵中心 [1]
              [1, 3, 14, 9, 1]  
              [12, 3, 4, 5, 2]   
然后把每一圈从小到大排列一下， 然后顺时针再填充回矩阵里。
'''
import collections, math
grid = [[-1,3,5,6,7,9,9,9], 
        [-2,3,4,5,2,9,9,9], 
        [-3,9,1,2,3,9,9,9], 
        [1,3,14,9,1,9,9,9], 
        [12,3,4,5,2,9,9,9]]

m, n = len(grid), len(grid[0])
layers = collections.defaultdict(list)

def spiral(grid, lev, m, n):
    k = min(n, m)
    if k % 2 == 1:
        if m == k and lev == k // 2:
            return [(lev, y) for y in range(lev, n - lev + 1)]
        if n == k and lev == k // 2:
            return [(x, lev) for x in range(lev, m - lev + 1)]
    x = y = lev
    res = []
    res.append((x, y))
    while y + 1 < n - lev:
        y += 1
        res.append((x, y))
    x += 1
    while x < m - i:
        res.append((x, y))
        x += 1
    x -=1
    y -= 1
    while y >= i + 0:
        res.append((x, y))
        y -= 1
    y += 1
    x -= 1
    while x >  i + 0:
        res.append((x, y))
        x -= 1
    return res

l = math.ceil(min(m, n) / 2)
for i in range(l):
    arr = []
    lst = spiral(grid, i, m, n)
    layers[i] = lst
    for x, y in lst:
        arr.append(grid[x][y])
    arr = sorted(arr)
    # # print(arr)
    # print('##',lst)
    # print('##',arr)
    for i in range(len(lst)):
        x, y = lst[i]
        grid[x][y] = arr[i]

print(layers)
print(grid)
'''
{
    0: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0)], 
    
    1: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 6), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (2, 1)]

    2: [(2, 2), (2, 3), (2, 4), (2, 5), (2, 4), (2, 3), (2, 2)]
    }


    [
        [-3, -2, -1, 1, 2, 3, 3, 4], 
        [12, 1, 2, 3, 3, 4, 5, 5], 
        [9, 14, 1, 2, 3, 9, 9, 5], 
        [9, 9, 9, 9, 9, 9, 9, 6], 
        [9, 9, 9, 9, 9, 9, 9, 7]]
'''



'''#3. 
一个2d char矩阵包含3种类型（'#'->barrier; '.'->emptySpace; '*'->figure) 假设所有的figure整体朝下落，落的过程中figure碰到barrier就把barrier摧毁 问要使至少一个figure落到最下面一行(i=R-1)会摧毁几个barrier. （存一下每列当前最靠下的figure的i，遇到barrier计算一下头顶即可）
  e.g.  [ *  *  * ]    -> output = 3
        [ .  X  * ],
        [ X  .  ‍‌‌‌‌‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌* ],
        [ *  *  . ],
        [ .  .  . ],
        [ .  X  X ],
'''
import collections
grid = [['*','*', '*'],
        ['.', '.','.'],
        ['.','#', '*'],
        ['#','#', '*'],
        ['*','*', '.'],
        ['.','.', '.'],
        ['.','#', '#'],
]
m, n = len(grid), len(grid[0])
col = collections.defaultdict(list)
d = -1
for j in range(n):
    for i in range(m - 1, -1, -1):
        if grid[i][j] == '*':
            col[j].append(i)
            d = max(d, i)
d = m - d - 1
print(col)
print(d)
res = 0
for c, lst in col.items():
    for f in lst:
        print(f)
        for i in range(f, f+d+1):
            if 0 <= i < m and grid[i][c] == '#':
                res += 1
print('final: ', res)



'''  3 A6
第一题， 给一整数n 返回一个 n*n二维数组， 第一行最后一行都是* ， 中间每一行只有第一列最后一列是*
e.g.
'''
n = 4
n = 2
res = [[' '] * n for _ in range(n)]
for i in range(n):
    if i == 0 or i == n - 1:
        for j in range(n):
            res[i][j] = '*'
    else:
        res[i][0] = '*'
        if res[i][-1] != '*':
            res[i][-1] = '*'

print(res)