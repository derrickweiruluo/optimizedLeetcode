'''
An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.


'''


class UndergroundSystem:

    def __init__(self):
        self.check_in_id = {}
        self.time_pairs = collections.defaultdict(int)  # totoal time spent in two specific station
        self.freqs = collections.defaultdict(int)       # totoal freqs between two specific station

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # A customer with a card ID equal to id, checks in at the station stationName at time t.
        # A customer can only be checked into one place at a time.
        self.check_in_id[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # A customer with a card ID equal to id, checks out from the station stationName at time t.
        check_in_station, check_in_time = self.check_in_id[id]
        self.time_pairs[(check_in_station, stationName)] += t - check_in_time
        self.freqs[(check_in_station, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Returns the average time it takes to travel from startStation to endStation.
        return self.time_pairs[(startStation, endStation)] / self.freqs[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)