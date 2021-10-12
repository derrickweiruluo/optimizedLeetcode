"""
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

################

Constraints:

1 <= timestamp <= 2 * 109
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.
"""

### 面试问到的话，问清楚怎么定义last 5 min

class HitCounter:

    def __init__(self):
        self.hitCounter = collections.Counter()
        

    def hit(self, timestamp: int) -> None:
        self.hitCounter[timestamp] += 1
        

    def getHits(self, timestamp: int) -> int:
        # ex: for time btw 1 to 300 
        # O(n) for the below accumulating
        # for i in range(timestamp - 299, timestamp + 1):
        #     res += self.counter[i]
        res = 0
        for t in range(timestamp - 299, timestamp + 1):  # from relative idx 0 to 299
            res += self.hitCounter[t]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
