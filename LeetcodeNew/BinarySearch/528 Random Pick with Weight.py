'''
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
'''

class Solution:

    def __init__(self, w: List[int]):
        # self.total = sum(w)
        self.n = len(w)
        for i in range(1, self.n):
            w[i] += w[i - 1]
        self.w = w

    def pickIndex(self) -> int:
        random_weight = random.randint(1, self.w[-1])
        left, right = 0, self.n - 1
        while left < right:
            mid = (left + right) // 2
            if self.w[mid] < random_weight:
                left = mid + 1
            else:
                right = mid
        return left