class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       return 

class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y


# 很明显，我们将二维平面划均分为四个区域，然后给自递归处理，计算每个区域的countShips，然后累积起来。

# 需要注意的几点：
# （1）划分区域的时候需要保证四块的边界不能重复。
# （2）提前用hasShip来预判是否有船在区域内，如果没有，可以直接返回零。（
# 3）边界条件是：当左上角与右下角重合时，返回的结果与hasShip的结果一致。
# (4)在调用hasShip之前，需要保证右上角和左下角的相对位置关系是正确的：比如当右上角是[0,1]且左下角是[0,0]时，其实并不能分出四个区域，其实两个区域是“假的“，并不能调用 hasShip.


# (This problem is an interactive problem.)

# Time O(10logMN)
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        res = 0
        TR, BL = topRight, bottomLeft
        
        if TR.x >= BL.x and TR.y >= BL.y and sea.hasShips(TR, BL):
            if TR.x == BL.x and TR.y == BL.y:
                return 1
            midX, midY = (TR.x + BL.x) // 2, (TR.y + BL.y) // 2
            res += self.countShips(sea, TR, Point(midX + 1, midY + 1))
            res += self.countShips(sea, Point(midX, TR.y), Point(BL.x, midY + 1))
            res += self.countShips(sea, Point(midX, midY), BL)
            res += self.countShips(sea, Point(TR.x, midY), Point(midX + 1, BL.y))
        
        # 终结搜索了，就return res, 最底层 rect 缩到 0 的时候， 自动skip 掉 for loop
        return res



# 不要用这个解法
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        TR, BL = topRight, bottomLeft
        return sum(BL.x <= x <= TR.x and BL.y <= y <= TR.y for x, y in sea._Sea__ans)