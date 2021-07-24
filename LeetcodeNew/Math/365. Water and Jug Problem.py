# GCD of 24 and 18 is 6

# GCD of x, y:
#   while y != 0:
#     x, y = y, x % y

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        x, y = jug1Capacity, jug2Capacity
        
        if x + y < targetCapacity:
            return False
        if x == targetCapacity or y == targetCapacity:
            return True
        
        # if target can by a multiplier of the gcd
        return targetCapacity % gcd(x, y) == 0
    
    
    # gcd fucntion, pure math
    
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        
        return x
        
