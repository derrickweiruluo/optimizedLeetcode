'''
Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].

'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < k: return False
        if sum(nums) % k != 0: return False
        
        target = sum(nums) / k
        visited = [0] * n
        nums.sort(reverse = True)
        
        def dfs(k, index, currSum):
            if k == 1:
                return True
            if currSum == target:
                return dfs(k - 1, 0, 0)
            
            for i in range(index, n):
                if visited[i] == 0 and currSum + nums[i] <= target:
                    visited[i] = 1
                    if dfs(k, i + 1, currSum + nums[i]):
                        return True
                    visited[i] = 0
            
            return False
                    
        
        return dfs(k, 0, 0)