class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        seen = {0: -1}
        curr_remainder = 0
        
        for idx, val in enumerate(nums):
            curr_remainder = (curr_remainder + val) % k   # MOST IMPORTANT
            if curr_remainder not in seen:
                seen[curr_remainder] = idx
            else:
                # this a step to make sure valid range: len > 2
                # corner cases:
                # if only the first one iteself satisfy, len == 1: False
                # if the first two together satisfy:     len = 2 - 0 > 1: True
                if idx - seen[curr_remainder] > 1:      # remainder check is 左闭右开，所以要 > 1才符合
                    print(idx, seen[curr_remainder])
                    return True
        
        return False
        
        
        

# Explanation:
# cur calculate the prefix sum remainder of input array A
# seen will record the first occurrence of the remainder.
# If we have seen the same remainder before,
# it means the subarray sum if a multiple of k


# Complexity
# Time O(N)
# Space O(N)

    
# Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n)
