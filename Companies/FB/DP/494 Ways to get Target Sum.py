'''
必须使用所有数字，只 穿插 + - 号，问有多少种方法 reach target SUm


Input: nums = [1,1,1,1,1], target = 3
Output: 5

Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
'''




""":
To make it clear for everyone, find following the syntax for get() method of dictionary(hase map)

It uses a dictionary to store all possible sums using all the numbers 
with +/- signs and return the number of ways of the target sum in the dictionary
"""


# Clarification:
# 必须使用所有数字，只 穿插 + - 号，问有多少种方法 reach target SUm
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
         
        prev_counter = collections.Counter({0: 1}) # start from 0


        for num in nums:
            step = collections.Counter()
            for y in prev_counter:
                step[y + num] += prev_counter[y]
                step[y - num] += prev_counter[y]
            
            prev_counter = step  # update the prevCounter after each iteration
        
        return prev_counter[target]