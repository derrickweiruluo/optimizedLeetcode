'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.


Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
'''

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        # {stop: bus_#}
        mapping = collections.defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                mapping[stop].add(bus)
        
        bfs = [(source, 0)]
        seen = set([source])
        
        for stop, bus_count in bfs:
            if stop == target:
                return bus_count
            for bus in mapping[stop]:
                for next_stop in routes[bus]:   # bfs the entire route 
                    if next_stop not in seen:
                        seen.add(next_stop)
                        bfs.append((next_stop, bus_count + 1))
                
                # clear the route upon finishing the bfs of this route, prevent cycling
                routes[bus] = []
        
        return -1