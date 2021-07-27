class UndergroundSystem:

    def __init__(self):
        self.check_in_id = {}
        self.time_pairs = collections.defaultdict(int)  # totoal time spent in two specific station
        self.freqs = collections.defaultdict(int)       # totoal freqs between two specific station

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_id[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_time = self.check_in_id[id]
        self.time_pairs[(check_in_station, stationName)] += t - check_in_time
        self.freqs[(check_in_station, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time_pairs[(startStation, endStation)] / self.freqs[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
