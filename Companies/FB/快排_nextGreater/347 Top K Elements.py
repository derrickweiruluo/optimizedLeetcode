'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


There are solution, using quickselect with O(n) complexity in average, but I think they are overcomplicated: actually, there is O(n) solution, using bucket sort. The idea, is that frequency of any element can not be more than n. So, the plan is the following:

Create list of empty lists for bucktes: for frequencies 1, 2, ..., n.
Use Counter to count frequencies of elements in nums
Iterate over our Counter and add elements to corresponding buckets.
buckets is list of lists now, create one big list out of it.
Finally, take the k last elements from this list, these elements will be top K frequent elements.
'''

''' Constraints:重要，唯一解
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''


# Clarifications:
# It is guaranteed that the answer is unique.
# which means, no conflict if there is tie

# Complexity: time complexity is O(n), because we first iterate over nums once and create buckets, then we flatten list of lists with total number of elements O(n) and finally we return last k elements. Space complexity is also O(n).

# Optimized bucket sort with two hashtables
import collections
class Solution:  # both O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # It is guaranteed that the answer is unique.
        # which means, no conflict if there is tie
        
        # bucket sort: https://leetcode.com/submissions/detail/602987983/
        
        counter = collections.Counter(nums)
        buckets = collections.defaultdict(list)
        maxFreq = 0
        
        res = []
        
        for num, freq in counter.items():
            maxFreq = max(maxFreq, freq)
            buckets[freq].append(num)
        
        for freq in range(maxFreq, -1, -1):
            if freq in buckets:
                res += buckets[freq]
            if len(res) == k:
                return res




class Solution:  # bucket sort, O(N) both
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # bucket of frequency from 0 to n, each freq has a [] to store num
        buckets = [[] for _ in range(len(nums) + 1)]
        counter = collections.Counter(nums)
        
        for num, freq in counter.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
            if len(res) == k:
                return res
        
        return res