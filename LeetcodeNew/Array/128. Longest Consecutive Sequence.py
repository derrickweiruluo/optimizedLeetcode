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
