import math

class Solution:  #1870
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right = 1, 10**7 + 1
        
        while left < right:
            mid = (left + right) // 2
            if self.helper(mid, dist, hour):
                right = mid
            else:
                left = mid + 1
                
        return -1 if left == 10**7 + 1 else left
    
    
    def helper(self,speed, dist, hour):
        time = 0
        for i in range(len(dist) - 1):
            if time > hour: return False
            time += math.ceil(dist[i] / speed)
            # cur_dist = dist[i]
            # if cur_dist % speed == 0:
            #     time += cur_dist // speed
            # else:
            #     time += (cur_dist // speed + 1)
        
        time += dist[-1] / speed
        return time <= hour
