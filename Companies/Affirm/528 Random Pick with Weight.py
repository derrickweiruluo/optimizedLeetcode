'''
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
'''


'''
EXAMPLE: 
Before: [1,6,2]
After:  [1,7,9]
by ratio: (0, 1], (1, 7], (7, 9]

follow up:
what if only the unique value matters (number of occurance does not matter). that is, 5 is 50% ‍‌‌‌‌‌‌‌‌‌‌‍‍‌‍‍‌‌‌‌and 6 is 50% at this time.
'''

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]
        self.total = self.w[-1]
        self.n = len(w)

    def pickIndex(self) -> int:
        randWeight = random.randint(1, self.total)
        left, right = 0, self.n - 1
        while left < right:
            mid = (left + right) // 2
            if self.w[mid] < randWeight:
                left = mid + 1
            else:
                right = mid
        return left





class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]
        self.total = self.w[-1]
        self.n = len(w)

    def pickIndex(self) -> int:
        randWeight = random.randint(1, self.total)
        left, right = 0, self.n - 1
        while left <= right:  # BS Template #1
            mid = (left + right) // 2
            if self.w[mid] == randWeight:
                return mid
            if self.w[mid] < randWeight:
                left = mid + 1
            else:
                right = mid - 1
        return left


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]
        self.total = self.w[-1]
        self.n = len(w)

    def pickIndex(self) -> int:
        randWeight = random.randint(1, self.total)
        left, right = 0, self.n - 1
        while left < right:
            mid = (left + right) // 2
            if self.w[mid] < randWeight:
                left = mid + 1
            else:
                right = mid
        return left