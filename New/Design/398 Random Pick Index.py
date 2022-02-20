'''
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
'''

# Clarifications:
# Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

class Solution:  # Approach 3: Reservoir sampling
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        n = len(self.nums)
        cnt = 0
        idx = 0
        for i in range(n):
            if self.nums[i] == target:
                cnt += 1
                if random.randint(0, cnt - 1) == 0:
                    idx = i
        
        return idx

# Reservior Sampling:
# Examples: [1,1,1], idx = 0, 1, 2

# 最后 return idx = 0 的概率是: 1 * 1/2 * 2/3 --> (T, F, F)
# 最后 return idx = 1 的概率是: 1/2 * 2/3 --> (T, F) 不管之前发生了什么
# 最后 return idx = 2 的概率是: 1/3 --> (T), 不管之前发生了什么



        
# Hashmap O(N) space solution
class Solution:

    def __init__(self, nums: List[int]):
        self.dic = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:
        lst = self.dic[target]
        return random.choice(lst)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)