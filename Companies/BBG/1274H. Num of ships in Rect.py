

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       return 

class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y




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
        
        return res