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
