"""
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

#######.   Priority Queue, O(NlogN).   ##########
i is the index of next stops to refuel.
res is the times that we have refeuled.
pq is a priority queue that we store all available gas.

We initial res = 0 and in every loop:

We add all reachable stop to priority queue.
We pop out the largest gas from pq and refeul once.
If we can't refuel, means that we can not go forward and return -1
"""

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        maxHeap = []
        res, idx = 0, 0
        curr_fuel = startFuel
        
        while curr_fuel < target:
            """
            the below while loop is to, at curr_fuel, the furthest station can reach
            and continueusly construct the gas max Heap for the entire trip
            """
            while idx < len(stations) and curr_fuel >= stations[idx][0]:
                heapq.heappush(maxHeap, -1 * stations[idx][1])
                idx += 1

            if not maxHeap: return -1
            curr_fuel += -1 * heapq.heappop(maxHeap)
            res += 1
        
        return res
