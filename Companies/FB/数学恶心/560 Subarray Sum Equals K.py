'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
'''

import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        counter = collections.Counter()
        counter[0] = 1
        res = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            res += counter[curSum - k]
            counter[curSum] += 1
        
        return res


###### FOLLOW UP ########



###### FOLLOW UP ########

class Solution: 
    def subarraySum(self, nums: List[int], k: int) -> list[int]:
        cumSum_mapping = collections.defaultdict(list)
        cumSum_mapping[0] = [-1]
        curSum = 0
        res, resIndices = 0, []
        for j, num in enumerate(nums):
            curSum += num
            for i in cumSum_mapping[curSum - k]:
                resIndices.append(nums[i + 1: j])
                res += 1
            cumSum_mapping[curSum].append(j)
        
        return res
        # return resIndices