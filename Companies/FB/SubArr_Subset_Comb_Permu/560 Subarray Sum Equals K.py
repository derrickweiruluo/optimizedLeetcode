'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

'''

# Similar to 974

class Solution:  # SAME
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        preSum = collections.Counter()
        preSum[0] = 1  # 这一部很需要，prefix == 0 要 intialize 为 1
        curSum = 0
        
        for num in nums:
            curSum += num
            res += preSum[curSum - k]
            preSum[curSum] += 1
        
        return res


class Solution:  # Follow up on return all subArray
    def subarraySum(self, nums, k): 
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



class Solution: # SLiding Window O(n^2)__ONLY work for positive numbers
    def subarraySum(self, nums: List[int], k: int) -> int: 
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0

        # O(n^2) solution
        count = 0
        i, j = 0, 1
        while j < len(nums):
            sub = nums[i:j+1]
            if sum(sub) == k: # increment count and then disturbe the window again
                count += 1         # --- or return True
                j += 1 # disturbacne
            elif sum(sub) < k:      # --- expand
                j += 1
            else: # shrink
                i += 1

        return count # return False

### TLE
class Solution2: # O(n^2), O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                if cur == k:
                    res += 1
    
        return res