'''
An underground railway system is keeping track of customer travel times between different stations. 
They are using this data to calculate the average time it takes to travel from one station to another.
'''

import collections
class UndergroundSystem:

    def __init__(self):
        self.checkInMapping = {}        # {id: start, timestamp}
        self.timeMapping = collections.defaultdict(int)  # {(start, end) : tot_time}
        self.freqMapping = collections.defaultdict(int)  # {(start, end) : tot_freq}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMapping[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, time = self.checkInMapping[id]
        self.timeMapping[(startStation, stationName)] += t - time
        self.freqMapping[(startStation, stationName)] += 1

        self.checkInMapping.pop(id)     # Optimization of Space 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = self.timeMapping[(startStation, endStation)]
        count = self.freqMapping[(startStation, endStation)]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)