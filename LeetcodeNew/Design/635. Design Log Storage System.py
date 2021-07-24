class LogSystem:

    def __init__(self):
        self.times = []
        self.granu = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id: int, timestamp: str) -> None:
        self.times.append([timestamp, id])

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        granu = self.granu[granularity]
        start, end = start[:granu], end[:granu]
        return [logId for timestamp, logId in self.times if start <= timestamp[:granu] <= end]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
