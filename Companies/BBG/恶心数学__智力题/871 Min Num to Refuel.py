'''
A car travels from a starting position to a destination which is target miles east of the starting position. (给初始油量，一路向北，到达 XX miles之外)

one fuel / one mile

The gas stations are represented as an array stations where: 
    stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.


Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.
'''



# i is the index of next stops to refuel.
# res is the times that we have refeuled.
# pq is a priority queue that we store all available gas.

# We initial res = 0 and in every loop:

# We add all reachable stop to priority queue.
# We pop out the largest gas from pq and refeul once.
# If we can't refuel, means that we can not go forward and return -1


# Clarifiction:
# 到站刚刚没油了，也是valid
# 到终点刚刚没油了，也是valid

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxHeap = []
        idx = 0
        res = 0
        cur = startFuel
        
        while cur < target:
            while idx < len(stations) and cur >= stations[idx][0]:
                heapq.heappush(maxHeap, -1 * stations[idx][1])  # while 可以到达，预存之前每个站的油
                idx += 1
            
            if not maxHeap: return -1
            cur += heapq.heappop(maxHeap) * (-1)        # 不可到达时，pop heap最大的，如果heap空了就return -1
            # 加了一次油就会进入下一个outer while loop
            res += 1
        
        
        return res