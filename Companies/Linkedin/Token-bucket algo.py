import datetime

class TokenBuck:
    def __init__(self, maxBucketSize, refillrate):
        self.maxBucketSize = maxBucketSize
        self.refillrate = refillrate
        self.currentBucketSize = maxBucketSize
        self.lasRefillTimeStamp = datetime.now()

    def allowRequest(self, tokens):
        self.refill()
        if self.currentBucketSize > tokens:
            self.currentBucketSize -= tokens
            return True
        return False

    def refill(self):
        curTime = datetime.now()
        toeknsAdded = (curTime - self.lasRefillTimeStamp) * self.refillrate / 10 ** 9
        self.currentBucketSize = min(self.currentBucketSize + toeknsAdded, self.maxBucketSize)
        self.lasRefillTimeStamp = curTime