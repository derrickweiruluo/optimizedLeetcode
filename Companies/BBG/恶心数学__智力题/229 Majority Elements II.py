'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Input: nums = [3,2,3]
Output: [3]

Input: nums = [1]
Output: [1]

Input: nums = [1,2]
Output: [1,2]

'''

# Clarification: Might have no answer
# O(1) space
# 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # return all elements appear more than floor(n / 3) times
        # O(1) Space
        
        # step 1: # find nums with top 2 frequency
        first, second = -math.inf, -math.inf
        firstCnt, secondCnt = 0, 0
        for num in nums:
            if first == num:
                firstCnt += 1
            elif second == num:
                secondCnt += 1
            elif firstCnt == 0:
                first = num
                firstCnt += 1
            elif secondCnt == 0:
                second = num
                secondCnt += 1
            # 画龙点睛， 通过 cnt -= 1 确保candidate都是majority
            else:
                firstCnt -= 1
                secondCnt -= 1
        
        # Step 2: count the frequencies of the top 2
        firstCnt, secondCnt = 0, 0
        for num in nums:
            if first == num:
                firstCnt += 1
            elif second == num:
                secondCnt += 1
        
        # step 3: there could be zero to two Majority Elements
        res = []
        target = floor(len(nums) / 3)
        if firstCnt > target: res.append(first)
        if secondCnt > target: res.append(second)
            
        return res