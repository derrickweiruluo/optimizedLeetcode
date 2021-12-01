'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''

'''
First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that. Since we check each streak only once, this is overall O(n). 
'''

class Solution:  #一样的解,小小的cleanup而已
    def longestConsecutive(self, nums: List[int]) -> int:
        # https://leetcode.com/submissions/detail/531368877/
        # https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
        

        # only check the increasing streak, at num when num - 1 is valid, we skip
        # it because eventually, we will scan the increasing streak from its min
        if not nums:
            return 0
        
        validNums = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in validNums:
                nextNum = num + 1
                if nextNum not in validNums:
                    continue
                else:
                    while nextNum in validNums:
                        nextNum += 1
                    res = max(res, nextNum - num)
        
        return res if res else 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
# First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.

# Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that. Since we check each streak only once, this is overall O(n). This ran in 44 ms on the OJ, one of the fastest Python submissions.
        
        if not nums: return 0
        
        nums_set = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in nums_set:             # for consec seq 4, 1, 3, 2, ony start counting at the lowest num in a seq
                if num + 1 not in nums_set:         # both -1, + 1 not exisit 
                    continue
                else:
                    next_num = num + 1                    
                    while next_num in nums_set:
                        next_num += 1
                    res = max(res, next_num - num)
                # print(res)
        
        return res if res != 0 else 1