import collections, math
from typing import Tuple
'''     1. *
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=728695 // 
 给定一个数组，返回一个zigzag数组， a[i] < a[i+1] > a[i+2] || a[i] > a[i+1] < a[i+2] => true。

Ex. [1,3,4,2,5]
return [false, true, true]
'''
arr = [1,3,4,2,5]
res = [False] * (len(arr) - 2)
for i in range(1, len(arr) - 1):
    if arr[i - 1] < arr[i] and arr[i] > arr[i + 1] or arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
        res[i - 1] = True
print(res)

'''   ✨✨✨✨  2. * 
根据以下算法处理string 1）if s.length <= 3, return 2) if s.length > 3, split 成multiple subtring, 每个substring的length 是3 3）
replace every substring with the sum of every digit, continue with 2) until 1) 

Ex, str = "11122223445" 
012 345 678 9 
111 222 333 4 
end index of each chunk: 0+2, 3+2, 6+2, 9+2 
2 -> "111" "222" "234" "45" 
3 -> "3" "6" "9" "9" -> "3699" 
2 -> "369" "9" 
3 -> "18" "9" -> "189" 
return "189"
'''
s = "11122223445"
output = ''
while len(s) > 3:
    cur = ""
    res = 0
    for i in range(len(s)):
        res += int(s[i])
        if i % 3 == 2 or i == len(s) - 1:
            cur += str(res)
            res = 0
    s = cur
print(s)



'''  ✨✨✨✨ 3. *** 频率：2 
/* 给一个matrix, 找出所有radius = k的sum的三个最大值 radius的定义是像上下左右辐射k个距离的菱形
'''
# 菱形题目， 找半径为k的最大的三个菱形面积
import heapq
matrix = [[1,2,3,9,0],[0,1,2,3,5],[3,4,5,6,7]]
k = 1
m, n = len(matrix), len(matrix[0])
heap = []

def area(grid, x, y, k):
    res = 0
    for i in range(x - k, x + k + 1):
        diff = abs(x - i)
        for j in range(y- k + diff, y + k - diff + 1):
            res += grid[i][j]
    return res

for i in range(1, m - 1):
    for j in range(1, n - 1):
        cur = area(matrix, i, j, k)
        heap.append(-cur)
res = []
heapq.heapify(heap)
for i in range(3):
    res.append(-1 * heapq.heappop(heap))
print(res)


'''    ✨✨  4. ** 频率：2
There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 2 consecutive stones where piles[i] = piles[i+1]. The game continues until noboday can make any move. return winner 
Ex. [1,2,2,3,3,1,1] Alice take [2,2], Bob [3,3], Alice [1,1]. 剩下一个1没办法take，Alice 赢 */ // 翻译：就是轮流从数组中拿相邻的值又相同的一对，直到拿完为止，最后一个拿的获胜 // 我的思路：brute force每轮从头遍历到尾，找到相邻的相同一对删除，直到不能删
'''

stones = [1,2,2,3,3,1,1]
i = j = 0
player = -1 # for default, if cur player can take one pair, -1 --> 1
n = len(stones)
stack = []
res = -1
while i < n:
    if not stack or stack[-1] != stones[i]:
        stack.append(stones[i])
    else:
        stack.pop()
        res *= -1
        print(res)
    i += 1
print('final winner is: ', res)


'''
5. * 频率：3
/* checkMonotonicity(easy)
Q: Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A <= A[j]. An array A is monotone decreasing if for all i <= j, A >= A[j].
Return “True” if the given array A is monotonic else return “False” (without quotes).
Input : 6 5 4 4     --> True
Input : 5 15 20 10  --> False

检查array 是否单调递增或递减, 是就回传true, 5分钟搞定吧。*/
'''
arr = [2,2,5,7,7,32,54,100,100]
# arr = [5, 15, 20, 10]
n = len(arr)
up = down = True
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        down = False
    if arr[i] < arr[i - 1]:
        up = False

print(up or down)

'''     6. * sumofReversed(easy)
Q: 给定一个numbers arrays of array, 将裡面所有number 按照题目规则reverse后，将所有结果加总。
Example:
Input: numbers =[ [7, 20, 73200], [12, 23, 15]]
                  23700 + 20 + 7  21 + 32 + 51
Output: 23709 + 104 = 23813
'''
input = [[7, 20, 73200], [12, 23, 15]]
res = 0
def convert(s):
    s = str(s)[::-1]            # 转换成reverse str
    i = 0
    while s[i] == '0':
        i += 1
    return str(s[i:]) + '0' * i # move all leading '0' to end
    
for arr in input:
    cur = 0
    for num in arr:
        cur += int(convert(num)) 
    print(cur)
    res += cur
    cur = 0

print(res)

'''     7. *************** 频率：2 俄罗斯方块变种

'''



'''     8.  * operations in array (easy)
Q: 给一个operations in array 以及一个numbers array, 有以下三种operations
第一种 [0, x]：将numbers都加上x
第二种 [1, x]：将numbers都乘以x
第三种 [2]: 从numbers中取出最小值加入result array
最后将result的和回传。
Input: numbers = [1, 12, 5, 7] operations = [[2], [0, 1], [1, 2], [2]]
Output:
Explain:
[2] => result = [1]
[0, 1] => numbers = [2, 13, 6, 8]
[1, 2] => numbers = [4, 26, 12, 16]
[2] => result = [1, 4]
return = 1 + 4 = 5
'''
import heapq
nums = [1, 12, 5, 7] 
ops = [[2], [0, 1], [1, 2], [2]]
res = 0
curMin = min(nums)
for op in ops:
    if len(op) == 1:
        res += curMin
        print(curMin)
    elif len(op) == 2:
        if op[0] == 0:
            curMin += op[1]
        else:
            curMin *= op[1]
print(res)


'''     9. **   二进制数字大数字加法
可能会特别大所以用string表示。求两个二进制数的和 sum(string s1, string s2); */
我的思路：经典大数加法
'''
a = "1010"
b = "1011"
carry = 0
res = ''
a, b = list(a), list(b)
while a or b or carry:
    if a:
        carry += int(a.pop())
    if b:
        carry += int(b.pop())
    res += str(carry % 2)
    carry = carry // 2

print(res[::-1])


'''10. *
把一个string 每两个char reverse 操作， e.g. abcde => badce
白给
'''
s = 'abcde' # --> 'badce
res = ''
for i in range(len(s)):
    if i % 2 == 0:
        if i != len(s) - 1:
            res += (s[i + 1])
            res += s[i]
        else:
            res += (s[i])
print(res)

'''     11. *  白给
给一个数组a, 返回数组b 表示a 中连续三个数是否是单调的， length(b) = length(a) - 2,
'''
nums = [1,2,3,4,5,6,7,8,0,2,4]

res = [False] * (len(nums) - 2)
for i in range(len(nums) - 2):
    if nums[i] <= nums[i + 1] <= nums[i + 2] or nums[i] >= nums[i + 1] >= nums[i + 2]:
        res[i] = True

print(res)

'''     12. * 频率：2 老题
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=726595
给一个String[], 需要用每一个String的第一个字母和下一个String的最后一个字母组成新String, 最后一个String和第一个String组
Example ["what“, "is", "your", "name"], output ["ws", "ir", "ye", "nt"]
'''
arr = ['what', 'is', 'your', 'name']
res = []
for i in range(len(arr)):
    if i == len(arr) - 1:
        res.append(arr[i][0] + arr[0][-1])
    else:
        res.append(arr[i][0] + arr[i + 1][-1])

print (res)

'''     13. **
给两个String[], 检查是否第二个String[]里所有的String都是第一个String[]里 
0 到 某个element的concatination 
String[] a, String[] b, check if b[j] = a[0] + a[1] +.. + a[i]

Example a = ["one", "twoThree", "four"], b = ["one", "onetwoThree"] true
a = ["one", "twoThree", "four"], b = ["onetwo"] false */

我的思路：把所有a数组从0到1，到2，到3......到n的字符串都算出来，存在hashset里，然后遍历b看看是不是每个元素都在里面
'''
a = ["one", "twoThree", "four"], b = ["onetwo"]
path = ''
valid = set()
for i in range(len(a)):
    path += a[i]
    valid.add(path)

res = True
for elem in b:
    if elem not in valid:
        print(False)
print(True)




'''   ✨✨✨✨ 14. *** 频率：2
给一个matrix 和一个int k, 找到所有总和最大的k * k的submatrix，返回这些subarray里的distinct element 
[[1, 2, 3]
 [3, 2, 1] k = 2, 有两个sum为8的submatrix, distinct element为{1, 2, 3}
 [0, 0, 0]]

'''
k = 2
grid = [[1,2,3,9,0],[0,1,2,3,5],[3,4,5,6,7]]
'''
[[1,2,3,9,0],
 [0,1,2,3,5],
 [3,4,5,6,7]]

 [[0, 0, 0,  0,  0,  0], 
  [0, 1, 3,  6,  15, 15], 
  [0, 1, 4,  9,  21, 26], 
  [0, 4, 11, 21, 39, 51]]
'''

import math
k = 2
grid = [[1,2,3,9,0],[0,1,2,3,5],[3,13,5,6,7]]
'''
[[1,2,3,9,0],
 [0,1,2,3,5],
 [3,13,5,6,7]]
'''

m, n = len(grid), len(grid[0])
preSum = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, len(preSum)):
    for j in range(1, len(preSum[0])):
        preSum[i][j] = grid[i - 1][j - 1] + preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1]

curMax = -math.inf
lst = []
for i in range(k, len(preSum)):
    for j in range(k, len(preSum[0])):
        cur = preSum[i][j] - preSum[i - k][j] - preSum[i][j - k] + preSum[i - k][j - k]
        if cur > curMax:
            curMax = cur
            lst = [(i - 1, j - 1)]
        elif cur == curMax:
            lst.append((i - 1, j - 1))

res = set()
print('maxArea is: ', curMax)
for x, y in lst:
    for i in range(x - k + 1, x + 1):
        for j in range(y - k + 1, y + 1):
            res.add(grid[i][j])

print(res)



'''    ✨✨ 15. * 频率：2
给一个int[] num, 然后定义rev是把一个数reverse, 例如rev(23) = 32,
求有多少个(i, j)可以满足num[i] + rev(num[j]) = num[j] + rev(num[i])
int[] num: [12, 34] => 12+43 = 34+21 count = 1

我的思路：
num[i] - rev(num[i]) = num[j] - rev(num[j])
先计算数组的reverse数组，然后与原数组相加，得到一个cha数组，遍历数组将相同的和存在map里记录个数
然后根据map的个数计算pair对数，和36题思路一毛一样
'''
counter = collections.Counter() # 

def reverse(s):
    i = 0
    while s[i] == '0':
        i += 1
    return int(s[i:] + '0' * i)

nums = [12,34]
for num in nums:
    reverseNum = reverse(str(num)[::-1])
    diff = num - reverseNum
    counter[diff] += 1

res = 0
for key, val in counter.items():
    if val > 1:
        # 数学公式 1-5之间两两组合的总个数
        res += val * (val - 1) // 2

print(res)


'''16. *
给定一个字符串s，找出符合s[i - 1] != s[ i ]且 s[ i ] != s[i+1] 且 s[i - 1] != s[i + 1]的三元组的个数
白给
'''

'''17. ** 频率：2
给定一个3行N列的整数矩阵，矩阵中只包含1-9这9个数字，假设有一个3 x 3的滑动窗口，从左到右滑过整个矩阵。
如果当前滑动窗口中的9个值刚好为1-9这9个数字（顺序无所谓），且没有出现过重复, 则认为是true，否则是false.
返回一个数组，按从左到右滑动的顺序依次填入true或false。
[
[1,2,3,4,5,6,7,8,9]
[1,2,3,4,5,6,7,8,9]
[1,2,3,4,5,6,7,8,9]]
'''
grid = [[1,3,7,4,4,7],[5,2,9,5,3,6],[4,8,6,2,1,9]]
totalCol = len(grid[0])
res = [False for i in range (totalCol - 2)]
print(res)
preSum = [[''] * len(grid[0]) for _ in range(len(grid))]
for i in range(len(grid)):
    for j in range(2, len(grid[0])):
        preSum[i][j] = str(grid[i][j]) + str(grid[i][j - 1]) + str(grid[i][j - 2])
print(preSum)
'''[
'', '', '731', '473', '447', '744'], 
['', '', '925', '592', '359', '635'], 
['', '', '684', '268', '126', '912']]
'''

for i in range(totalCol - 2):
    cur = set()
    for r in range(3):
        for c in range(i, i + 3):
            cur.add(grid[r][c])
    print(cur)
    if len(cur) == 9:
        res[i] = True

print(res)

'''     18. ******
/给你两个多维数组grid 和 strength，grid和strength的行列数是相同的，即如果grid 是 3 x 4，那么strength也是3 x 4。
grid里只包含 '*', '.', '#' 3种字符，*代表障碍物， #代表箱子，. 代表空格子
strength中的元素则代表grid中相应位置上如果是障碍物，则障碍物上方最多可以承受的箱子的个数
每个箱子的重量相同，障碍物的承重只看箱子个数（即strength中对应位置上的值）。
现在从上往下看，如果压在障碍物上面的格子数量超过了它的承重，那么障碍物会被压垮消失，
此时箱子会继续往下掉，直到遇到承重更强的障碍物或者到底了又或者是下面也是箱子（箱子可以摞起来）。
现在给定初始状态下的grid和strength，求最后grid的状态，返回修改之后的grid。 */
思路：遍历矩阵，每一列从上到下遍历，遇到空白无视，遇到箱子累加箱子个数，遇到障碍物判断是否能承受累加的重量，如果可以承受则从当前位置向上遍历写入value，累加数清零后继续遍历，如果不能承受则直接继续遍历，直到底部后向上写入。
'''

'''     19 *****/*
给你两个字符串，binaryString, request 长度可到10^5。
binaryString中只有'0'和'1'表示一个二进制数， request中只有 '-' 和 '?'。现在要求遍历request, 
如果发现当前字符是'-'，则binaryString所表示的二进制数要减去1,
如果当前字符是'?' 求当前binaryString所表示的正整数的二进制位为1的个数.
最后返回一个数组, 按request中出现？的顺序返回当前binaryString所表示的正整数中二进制位为1的个数。

思路：二进制思路
从最低位开始看，
1. 如果最低位是1，那么-1后最低位会变成0. 这样1的总数会少1个。
2. 如果最低位是0，那么-1之后最低位会变成1，再顺着最低位开始往前看，如果紧挨着的那个是1，就要把1变成0，这时1的总数不变（少一个，又加了一个）
3. 如果紧挨着的是0，就要把0变成1，再继续往前看直到遇到第一个1为止，此时把这个1变成0，这个过程中所有遇到的0都要变成1.
所以只要在一开始先遍历一次binaryString，得到1的个数，然后再按上述方法计算1的个数应该就可以了。这样可以不用先计算出10进制表示，避免超大整数溢出的问题。
'''
s = '1000'
s = list(s)
ops = ['?', '-', '?', '-', '?']
cnt = 0
for char in s:
    if char == '1': cnt += 1
for op in ops:
    if op == '?': print(cnt)
    else:
        if s[-1] == '1':
            s[-1] = '0'
            cnt -= 1
            print(s)
        else:
            idx = len(s) - 1
            s[idx] = '1'
            idx -= 1
            cnt += 1
            if idx >= 0 and s[idx] == '1':
                s[idx] = '0'
                cnt -= 1
            else:
                while idx >= 0 and s[idx] == '0':
                    cnt += 1
                    s[idx] = '1'
                    idx -= 1
                s[idx] = '0'
                cnt -= 1
            print(s)


s = '12345'
s[0] = '9'
print(s)


            



'''     20. * 频率：4 你刷过了
地理出现过很多次的三角形 - 简单判定 a+b>c, a+c>b, b+c>a即可
'''

'''     21. **** 俄罗斯方块老题 频率：3
/* 俄罗斯方块 - 给你一个m*n的空矩阵，给你一俄罗斯方块图序列，比如1代表 。。。。4个小方格， 2代表凸（也是四个小方格）
现在你需要根据序列把空矩阵填满。简单的遍历和暴力破解便可，这里需要优先考虑行而不是列
'''

'''     22. ***** 19 题变种 减变加
给你一个二进制string， 然后有两种操作，一种是求里面一共有多少个1， 另外一种是对当前数字加1.
函数类似于：public List<String> func(String num, String[] operations); */
'''

'''     23. * broken keyboard 老题 频率：2
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=723954
/* 給定一個text string, 以及一個letters list，找出所有words 可以完全由letters拼出來的
1. 每個單字都會被空格隔開
2. 單字裡頭有special characters的不用算
3. 單字會有大寫，但letters list裡頭只有小寫
ex: s = "Hello, world!", letters = ["h", "e", "l", "o"]

第一個字"Hello," 可以算，因為","不用被考慮
我有一個case沒過，不知道是什麼沒考慮到*/
思路：letters存在set里，对s进行lower()，然后遍历s的每一个字符看是否在set里。非字母跳过。
'''
s = 'AbCd, !123'
print(s.lower())
print(s.split())
for num in s: 
    print(num.isalpha(), num.isdigit(), num.isalnum())

s = "Hello, world!"
letters = ["h", "e", "l", "o"]
wordSet = set()
for c in letters: wordSet.add(c)

res = []
for sub in s.lower().split():
    cur = ''
    for char in sub:
        if char.isalpha():
            if char not in wordSet:
                print(char)
                break
            else:
                cur += (char)
    print(cur)
    if cur:
        res.append(cur)
print(res)



'''     24. 你刷过了
就是給m, n 以及start, goal point
從start 開始往斜對角走，碰到牆壁回彈
回傳走到goal point的距離，找不到的話回傳 -1 */
'''


'''     25. *** 频率：2
給一個array, 要求找出多少個subarray 可以滿足 最少有 >=k 的unique chars appeared only once
ex:
[1,2,3,4,1], k = 2
[1,2]
[1,2,3]
[1,2,3,4]
[2,3]
[3,4,1]
etc. */
第一想法：brute force
'''
# arr = [1,2,3,4,1,8,8,4,3]
arr = [1,1,1,1,1,1,1,1,10,1]
arr = [1,2,3,4,1]
k = 2
res = 0

for i in range(len(arr)):
    seen = set()  # 每次循环都清空set
    for j in range(i, len(arr)):
        if arr[j] not in seen:
            seen.add(arr[j])
        else:
            break   # start searching from next index
        if len(seen) >= k:
            res += 1
print(res)



'''     26. ***
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=723218
String的操作，有insert，copy，undo，paste，注意，undo只能返回上一次操作， insert x，插入x到当前string结尾处
copy，clipboard里存储当前string undo撤销上一次操作，不会出现连续的，只能撤销上一次的
paste粘贴clipboard中的string到结尾处 最后让你输出最后的string。
'''
cur = prev = ''
clipboard = ''
for op in ops:
    arr = op.split()
    if arr[0] == 'insert':
        prev = cur
        cur.append(arr[1])
    elif arr[0] == 'copy':
        clipboard = cur
    elif arr[0] == 'undo':
        cur = prev
    elif arr[0] == 'paste':
        prev = cur
        cur.append(clipboard)
print(cur)

'''     27. *
这个帖子👌
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=719472
给两个字符串，输出一个合起来的字符串，第一个的字符占偶数位第二个占奇数位，如果还有剩余就补在最后的结果后面
eg: given two strings, merge,
ex:
input: "abc", "12345", output: "a1b2c345"
input: "abc", "1", output: "a1bc"
'''
# a = 'abc'
a = 'abcdefg'
b = '12'
# b = '1234567'
na, nb = len(a), len(b)
l = min(na, nb)
res = ['-'] * l * 2
for i in range(l * 2):
    if i % 2 == 0:
        res[i] = a[i // 2]
    if i % 2 == 1:
        res[i] = b[i // 2]


print(res)
if na == nb: print(res)
rem = a[l:] if na > nb else b[l:]
print(rem)
print(''.join(res) + rem)


'''     28. * 频率：3
给一个长度为n的数组A，判断是不是由[1,2,...,n]或者[n,n-1,...,1]右移得来。比如[4,2,3,1]不是，[4,1,2,3]是
'''
# A = [7,9,10,2,3,6]
# A = [4,2,3,1]
A = [1,2,3]  # presorted

def isSorted(num):
    up = sorted(num)
    down = sorted(num, reverse = True)
    return num == up or num == down

if isSorted(A):  print('FINAL', False)
for i in range(len(A)):
    print(A[i:] + A[:i])
    if isSorted(A[i:] + A[:i]):
        print('FINAL', True)
print('FINAL', False)

'''29. * 频率：3 与24题相同
给你二维数组长和宽，起点坐标，终点坐标。一开始从起点按照(+1, +1)的方式走，x坐标出界就取相反数，y出界
同理，走到角落就同时取反。问走到终点的步数，如果走不到返回-1. */
'''


'''     30. * 频率：3
给一个数组，返回子数组个数，子数组满足：所有元素都出现至少2次。
比如[1,2,1,2,4]返回1（[1,2,1,2]），[1,2,3,3,3,2,4]返回4（[3,3], [3,3], [3,3,3], [2,3,3,3,2]）*/
'''
 
import collections
A = [1,2,3,3,3,2,4]
res = []
seen = set()
def dfs(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            cur = ''.join(map(str, nums[i : j]))
            if cur not in seen:
                res.append(cur)
                seen.add(cur)
dfs(A)
print(res)
cnt = 0
 
#[3,3], [3,3], [3,3,3], [2,3,3,3,2]
ans = []
for s in res[1:]:
    c = collections.Counter(s)
    if c[min(c)] >= 2:
        ans.append(list(map(int, s)))
 
print(ans)

'''     31. *
有a,b,c三个值，如果 a = b = c，则值乘以1000；如果 a = b 或者 b = c 或者 a = c， 则值乘以500；否则值乘以100。
给定a, b, c三个数，求最后的值
'''
nums = [200,200,300]
seen = set()
for num in nums: seen.add(num)
if len(seen) == 1:
    print([a * 1000 for a in nums])
if len(seen) == 2:
    print([a * 500 for a in nums])
if len(seen) == 3:
    print([a * 100 for a in nums])

'''     32. ** 频率：2
数组，每个数字都不相同，首先找到最小的峰值，然后作为第一个返回值，把最小峰值从原数组中删除，然后在新数组中再次找到最小峰值，以此 类推。
'''
import heapq
nums = [1,4,5,3,8,6]
res = []
print(res)
print(nums)
heapq.heapify(nums)
while nums:
    res.append(heapq.heappop(nums))
    # print(res)
print(res)
print(nums)

'''// 33.
判断两个string 是不是相似的。相似的定义是：
1）其中任意一个string 上任意两个char 可以swap
2）其中任意一个string 上任意两个char 出现的次数可以swap */
我的想法：没懂
'''

'''
// 34. **
给一个包含正负数的数组，求所有pair的sum是一个perfect square的数量。
比如 [-1, 0, 1, 18, 3]
pair里的i, j 的条件是i <= j, 就是说同一个数字能够重复使用，在这个例子里 最大的pair sum就是36 (18 +18)，那么有可能出现的 perfect square就有0, 1, 4, 9, 16, 25, 36
那么[-1, 1], [0,1],[1,3,], [18,18]就是所有的pair
输出为4.
我用了一个hashmap的解法，不知道为什么最后一个test case超时
'''
import collections, math
nums = [-1, 0, 1, 18, 3]
# square = collections.defaultdict(int)
square = set()
res = 0
for i in range(0,len(nums)):
    if nums[i] > 0:
        cur = math.sqrt(nums[i] * 2)
        if int(cur) == cur:
            print(nums[i], 'X2')
            res += 1
    for j in range(i):
        if nums[i] + nums[j] >= 0:
            root = math.sqrt(nums[i] + nums[j])
            if int(root) == root: 
                print(nums[i], nums[j])
                res += 1
##
print(res)

    
'''35. *** 老题 频率：3
新闻排版，input an array of lines, each line is an array of words. (array of array of string) 然后给你一个屏幕 宽度，每一行贪心地放 word，直到排满然后换行继续排，剩余的地方用空格去 padding，保证每一格都要凑够到屏幕宽度。没啥难的，就是细节比 较多（每一行前后都要加一个星号，最前面和最后面要加一排星号），写起来倒很快。
比如给你 [["hello", "world"], ["I", "love", "cats", "and", "dogs"]]，宽度 12，第一行左对齐第二行右对齐，要求输出

**************
*hello world *
* I love cats*
*    and dogs*
**************
'''
import math
input = [["hello", "world"], ["I", "love", "cats", "and", "dogs"]]
w = 14
charCount = 0
res = []
for arr in input:
    # res += arr
    res.extend(arr)
print(res)
spaces = len(res) - 1
charCount = sum(len(s) for s in res)
print(charCount, spaces)
r = 2 + math.ceil((charCount + spaces) / (w - 2))
print(r)

grid = [['*'] * w for _ in range(r)]
for i in range(1, len(grid) - 1):
    for j in range(1, w - 1):
        grid[i][j] = ' '

r = 1
c = 1
i = 0
while i < len(res):
    s = res[i]
    if len(s) + c < w - 1:
        for x in range(c, c + len(s)):
            grid[r][x] = s[x - c] 
        c += len(s) + 1
        i += 1
    else:
        r += 1
        c = 1
for i in range(2, len(grid) - 1):
    content = ''.join(grid[i][1:-1])
    last = 12
    while grid[i][last] == ' ': last -= 1
    content = content[last:] + content[: last]
    content = '*' + content + '*'
    grid[i] = list(content)
print(grid)

'''[
['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], 
['*', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', '*'], 
['*', 'I', ' ', 'l', 'o', 'v', 'e', ' ', 'c', 'a', 't', 's', ' ', '*'], 
['*', ' ', ' ', ' ', 'a', 'n', 'd', ' ', 'd', 'o', 'g', 's', ' ', '*'], 
['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
'''


'''     36. ***
给两个数组a和b，a的size和b的size相同，求对于pair i,j (i <= j)，
这两个数组里的pair的数量 应该是a[i]-b[j]=a[j]-b[i]
思路：变形为a[i] + b[i] = a[j] + b[j]，逻辑简单很多，我们只要把每个位置的和存下来看哪些是相同的即可，根据Map计算Pair的个数
'''
a = [1,2,3,4,5]
b = [4,3,2,1,10]
import collections
res = 0
freq = collections.defaultdict(int)
for i in range(len(a)):
    curSum = a[i] + b[i]
    freq[curSum] += 1
print(freq)
for pair, cnt in freq.items():
    if cnt >= 2:
        res += cnt * (cnt - 1) // 2
print(res)

'''37. *
给两个纯数字的字符串，如"987"和"654"，然后从最低位开始两两求和，输出最终的字符串，两个输入字符串都没有leading zeros。
如"987"和"654"输出"151311"，我是先把字符串转成int数组，然后安位求和，最后再转换回string。
'''
a = '987' 
b = '6543333'
leading = ''
l = min(len(a), len(b))
if len(a) > l:
    leading = a[: len(a) - l]
    a = a[len(a) - l:]
if len(b) > l:
    leading = b[: len(b) - l]
    b = b[len(b) - l:]
print(a, b, leading)
res = ''
for i in range(l):
    cur = int(a[i]) + int(b[i])
    res += (str(cur))

print(leading + res)

'''     38. *** 频率：2 老题
/* 给一个二维矩阵，每一行的第一列的数字，称之为pivot，要求对这些pivot进行排序。
排序的comparator不是基于这些pivot的值，而是他们的 “右上-右下-对角线sum”，
这个对角线sum的定义是，从这个pivot 开始向右上方挪动，到顶之后再像右下方挪动直到到达右边界或者下边界，
这样遍历下来的sum称之为对角线sum。
这道题，我是写一个子程序计算给定位置的pivot值，然后返回一个tuple(pivot,val)这里val是原始位置的值（因为这个是最后要输出的）
然后对第一列的每一行元素计算pivot，进行排序即可
思路：分别计算所有pivot的值，根据值排序原坐标
'''
A = [[1,2,3],[4,5,6],[7,8,9],[100,200,300]]

def pivot(A, i, j):
    res = A[i][j]
    dir = [-1, 1]
    m, n = len(A), len(A[0])
    while i > 0 and j < n - 1:
        i += dir[0]
        j += dir[1]
        res += A[i][j]
    dir = [1, 1]
    while i < m - 1 and j < n - 1:
        i += dir[0]
        j += dir[1]
        res += A[i][j]
    return res

nums = []
for i, arr in enumerate(A):
    p = pivot(A, i, 0)
    nums.append((arr[0], p))
print(nums)
res = [val for val, p in sorted(nums, key = lambda x: x[1])]
print(res)


'''     // 39. **** https://leetcode.com/problems/group-anagrams/
提供一个数组，数一下两两互为数字变形体的个数，
数字变形体的定义是，如果一个数把把它每一个数字位置改变就能和另一个数相同，它们就是数字变形体比如"123"和"321"和"312"都是数字变形体。
这道题我一开始写了个子函数，判断两个数字是否是变形体。然后暴力两层循环数一共有几对，通过了基本的测试，但是隐藏测试超时。
后来，对每一个数进行编码，比如123 = 1*100+1*10+1,1123=2*100+1*10+1，类似counting sort的思想，
这样直接比较两个数encoding后是否一样如果一样就是变形体，结果时间复杂度O(n^2)还是过不了所有的隐藏测试，
最后采用类似hash map的思路，建一个count字典，记录每个编码到目前为止出现的次数，遍历整个数组，
sum+=count[val]，最后返回sum。达到O(n)时间复杂度，通过了所有的测试。这道题类似力扣死侍酒。*/
思路：数字变形体的本质其实是所有数字加起来和相同，可以用和来编码记录每个编码的个数，最后遍历map计算个数。和36题本质相同。
'''
anagrams = collections.defaultdict(list)

for string in strs:
    key = ''.join(sorted(string))
    anagrams[key].append(string)

print(list(anagrams.keys()))
print(list(anagrams.values()))
print(anagrams.values())

'''     * 老题 频率：4  参考 https://leetcode.com/problems/rotate-image/
矩阵旋转老算法，提前记录对角线初始值，最后转完改回来就行
'''
import collections
k = 1
A = [[1,2,3],[4,5,6],[7,8,9]]
n = len(A)
times = k % 4
d = collections.defaultdict(int)
for i in range(n):
    d[(i, i)] = A[i][i]
    d[(i, -1 - i)] = A[i][-1 - i]


for i in range(times):
    A = [[row[i] for row in A[::-1]] for i in range(len(A))]
    # A = [list(col)[::-1] for col in zip(*A)]  另一种右旋转90度的 写法
print(A)
for (x, y), val in d.items():
    A[x][y] = val
print(A)


'''41. *** https://leetcode.com/problems/word-break/
地里的原题，给你一个list，给你另外一个list of list，问你从后面这个list of list里能否拼出前面这个list， 
比如 [3,2,5,1,4] 
[[5,1][3,2], [4]]就可以拼出来
'''
arr = [3,2,5,1,4]
lst = [[5,1],[3,2], [4]]
seen = set()
for l in lst:
    seen.add(''.join(map(str, l)))
print(seen)
dp = [False] * (len(arr) + 1)
dp[0] = True
for i in range(1, len(arr) + 1):
    for j in range(i):
        if dp[j] and ''.join(map(str, arr[j: i])) in seen:
            a = ''.join(map(str, arr[j: i]))
            print(a)
            dp[i] = True
            break
print(dp)

 
'''     **** 41 DFS solution (139. Word Break)
地里的原题，给你一个list，给你另外一个list of list，问你从后面这个list of list里能否拼出前面这个list， 
比如 [3,2,5,1,4] [[5,1][3,2], [4]]就可以拼出来'''
s = [3,3,3,2,5,1,4]
a = [[5,1],[3,2], [3],[4]]
s = ''.join(map(str, s))
wordSet = set()
memo = {}
for arr in a:
    wordSet.add(''.join(map(str, arr)))
res = True

def dfs(s, idx, wordSet, memo):
    if idx == len(s): return True
    if s[idx:] in memo: return memo[s[idx:]]
    for i in range(idx + 1, len(s) + 1):
        if s[idx: i] in wordSet and dfs(s, i, wordSet, memo):
            memo[s[idx:]] = True
            return True
    memo[s[idx:]] = False
    return False

res = dfs(s, 0, wordSet, memo)
print(res)

 
 
'''      42. **  (需要复习)
/* 给一个字符串，找到长度大于2的prefix， 且这个prefix是一个palindrome.
然后将这个前缀从字符串中删除。剩下的字符串重复之前操作，直到不能进行。比如： input: aaaabcbd output: d
解释： aaaabcbd -> aaaa 是最长的prefix, 长度大于2，且是palindrome， 所以将其删除，剩下的字符串是 bcbd,
bcbd -> bcb 是最长的prefix, 长度大于2，且是palindrome， 所以将其删除，剩下的字符串是 d
d -> d 是palindrome, 但是长度小于2， 所以不可以继续删除 */'''
 
s = 'aaaaabccd'
def valid(s):
  return s == s[::-1]
 
while len(s) >= 2:
    idx = 0
    for i in range(2, len(s) + 1):
        if valid(s[:i]):
            idx = i
    if s == s[idx:]:break
    s = s[idx:]

print('final == ', s)
 
 
'''**** 43. **** 频率：2 (similar to Leetcode 45)
input 是 两个数组 a,b, 两个整数lower, upper， 求这样的pair (i, j)，lower<= a * a + b*b <= upper, brute force 超时，
我sort了一下然后算left/right boundary， 也只过了8/13 要求 nlogn 否则超时 */
另一种描述：两个unsorted array，a 和 b 找 lower bound <= a[i] * a[i] + b[j] * b[j] >= upper bound。返回符合这个条件的一个有多少个
nlogn值得思考
我的思路：sort两个数组，固定一个另一个用binary search找范围。和45题非常类似。'''
import bisect
left, right = 50, 200
a = [1,2,3,4,5,6,7,32]
b = [3,6,10,14]

nums1 = [num ** 2 for num in sorted(a, key = lambda x: abs(x))]
nums2 = [num ** 2 for num in sorted(b, key = lambda x: abs(x))]
print(nums1)
print(nums2)

n = len(nums1)
m = len(nums2)
res = 0
for i in range(n):  # assuming a比较长
    left_bound, right_bound = left - nums1[i] - 0.01, right - nums1[i] + 0.01
    l = bisect.bisect_left(nums2, left_bound)
    r = bisect.bisect_right(nums2, right_bound)
    print(nums1[i], l, r)
    if l == m or r == 0: continue  # 无效情况： 左边界在尾端 or 右边界在头部
    len = r - l # 分开的计算的left right idx， 所以 r - l 就是长度
    res += len
print(res)



'''   44. ***
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=702470
You are given a string str containing only the letters W, D, and L. Your task is to construct a new string from the characters of str, according to the following algorithm:
1. Begin with an empty string output = "".
2. If str contains a W, then remove it and concatenate a W to the end of output.
3. If str contains a D, then remove it and concatenate a D to the end of output.
4. If str contains an L, then remove it and concatenate an L to the end of output.
5. If str is empty, end the algorithm; otherwise go back to step 2.
Return the value of output after the algorithm is complete.
Note that it doesn't matter from where you remove the letter from the string, only the count of the letters left in the string matters. */
翻译：输入是一个string，里面只有WDL三种字母，要根据这个string造一个新string。
从空string “” 开始，1. 如果遇到W，删除之并且在新string的结尾加一个W
2. 如果遇到D，删除之并且在新string的结尾加一个D
3. 如果遇到L，删除之并且在新string的结尾加一个L
这仨玩意儿是按顺序执行的，举个栗子：
For str = "LDWDL", the output should be equallyRearranging(str) = "WDLDL".
For str = "DLDD", the output should be equallyRearranging(str) = "DLDD".
input：DWWDWL ->output：WDLWDW
看着长其实白给 
'''
s = 'DWWDWL'
# s = 'DLDD'
# s = 'LDWDL'
res = ''
idx = 0
order = 'WDL'
while s:
    for i in range(len(s)):
        if s[i] == order[idx]:
            res += s[i]
            s = s[:i] + s[i + 1:]
            break
        # if idx == 1 and s[i] == 'D':
        #     res += s[i]
        #     s = s[:i] + s[i + 1:]
        #     break
        # if idx == 2 and s[i] == 'L':
        #     res += s[i]
        #     s = s[:i] + s[i + 1:]
        #     break
    idx = (idx + 1) % 3
print(res)


'''     45. **** 
https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
input：一个数组，找到能够分成三个连续不为空的subarray的个数，
条件：保证1st subarray的和 小于等于 2st subarray的和 小于等于 3st subarray的和
注意这里是一个数组只分成三个subarray，
ex: 输入：[1，2，3，3，0]
输出：符合条件的个数 --> [1],[2],[3,3,0] 符合+1， [1,2],[3],[3,0]符合+1 etc. */
'''
nums = [1,2,3,3,0]
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        nums = [1,2,3,3,0]
        res = 0
        for i in range(1, len(nums)):   # 先prefix sum
            nums[i] += nums[i - 1]

        j = k = 1   # boundary of the 2nd array
        for i in range(len(nums) - 2): #留两个空位给 第二第三
            while j <= i or j < len(nums) - 1 and nums[j] < nums[i] * 2:
                j += 1
            while k < j or k < len(nums) - 1 and nums[k] - nums[i] <= nums[-1] - nums[k]:
                k += 1
            midArrayLen = k - j
            res = (res + midArrayLen) % (10 ** 9 + 7)
        print(res)
        return res

'''https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=701576
// 46. ***** 股票机器银儿 leetcode: https://leetcode.com/problems/grumpy-bookstore-owner/
/* You've decided to create a bot for handling stock trades. For now, you have a simple prototype which handles trades for just one stock. Each day, it's programmed to either buy or sell one share of the stock.
You are given prices, an array of positive integers where prices[i] represents the stock price on the ith day. You're also given algo, an array of 0s and 1s representing the bot's schedule, where 0 means buy and 1 means sell.
In order to improve the bot's performance, you'd like to choose a range of k consecutive days where the bot will be programmed to sell; in other words, set a range of k consecutive elements from algo to 1. Your task is to choose the interval such that it maximizes the bot's total revenue. The revenue is defined as the sum of all selling prices minus the sum of all buying prices (in other words, the difference between the end and start amount). */
// NOTE: Assume you begin with enough shares of the stock that it's always possible to sell.
'''
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3

n = len(customers)
originalGain = 0
maxGain = curSave = 0

for i in range(n):
    # 叠加原来的gain when 老板开心
    if grumpy[i] == 0:
        originalGain += customers[i] 
    
    # sliding window of potential saving 
    curSave += grumpy[i] * customers[i] 
    if i > X - 1:
        curSave -= customers[i-X] * grumpy[i-X] # 左边界被减去得到新的 gain
    maxGain = max(maxGain, curSave)

print(originalGain + maxGain)


''' 47. ** 频率：3 https://leetcode.com/problems/spiral-matrix/
// 给一个NxN 的矩阵, 一圈一圈从外到内分别排序然后放回原大小的矩阵, 返回这个新的矩阵. 类似lc54
// 下面这个不是答案，是洋葱圈遍历
'''

#### in OA-2.py



'''     48. ** 频率：2
/* 两个数组的绝对差的定义：两个数组每个对应位置的数字的差的绝对值之和.
两个给定数组a, b, 保证长度相等, 然后a 中的每个数字可以被a 中任意不同位置的数字所代替,
在只允许在a 里最多做一次这种替代的情况下输出可能的最小的两个数组的绝对差 */
'''

a = [1,2,30]
b = [100, 200, 300]
res = 0
mapping = {}
for i in range(len(a)):
    mapping[i] = abs(a[i] - b[i])
    # res += abs(a[i] - b[i])

