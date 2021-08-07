"""
Explanation:
Python solution, but it's really easy to understand.
To make it clear for everyone, find following the syntax for get() method of dictionary(hase map)

It uses a dictionary to store all possible sums using all the numbers 
with +/- signs and return the number of ways of the target sum in the dictionary

"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
         
        prev_counter = collections.Counter({0: 1}) # start from 0
        for num in nums:
            step = collections.Counter()
            for y in prev_counter:
                step[y + num] += prev_counter[y]
                step[y - num] += prev_counter[y]
            
            prev_counter = step
        
        return prev_counter[target]
        
        
"""
    def findTargetSumWays(self, nums, S):   # solution #2
        count = defaultdict(int)
        count[0] = 1
        for x in nums:
            step = defaultdict(int)
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step

        return count[S]

"""    
