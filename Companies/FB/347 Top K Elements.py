'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


'''
'''
There are solution, using quickselect with O(n) complexity in average, but I think they are overcomplicated: actually, there is O(n) solution, using bucket sort. The idea, is that frequency of any element can not be more than n. So, the plan is the following:

Create list of empty lists for bucktes: for frequencies 1, 2, ..., n.
Use Counter to count frequencies of elements in nums
Iterate over our Counter and add elements to corresponding buckets.
buckets is list of lists now, create one big list out of it.
Finally, take the k last elements from this list, these elements will be top K frequent elements.
'''

''' Constraints:
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''


'''
Complexity: time complexity is O(n), because we first iterate over nums once and create buckets, then we flatten list of lists with total number of elements O(n) and finally we return last k elements. Space complexity is also O(n).
'''

class Solution:  # O(N) both
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
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