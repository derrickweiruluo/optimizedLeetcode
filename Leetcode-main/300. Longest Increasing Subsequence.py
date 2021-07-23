import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sortedSub = []
        
        # Increasing means same num will not be in the result, therefore use bisect_left
        for num in nums:
            idx = bisect_left(sortedSub, num)
            # idx == len means this num is the biggest
            if idx == len(sortedSub):
                sortedSub.append(num)
            else:
                # This is a Math规律, replace idx with a smaller num will always garantee the longest
                sortedSub[idx] = num
                
        
        return len(sortedSub)
