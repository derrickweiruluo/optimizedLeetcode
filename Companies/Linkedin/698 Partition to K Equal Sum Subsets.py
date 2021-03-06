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
# Backtracking


# I think the time complexity is O(k * 2^n), at least it's an upper bound. Because it takes the inner recursion 2^n time to find a good subset. Once the 1st subset is found, we go on to find the second, which would take 2^n roughly (because some numbers have been marked as visited). So T = 2^n + 2^n + 2^n + ... = k * 2^n.

# Space complexity: O(n)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total, n = sum(nums), len(nums)
        if n < k: return False
        if total % k != 0: return False
        
        target = total / k
        visited = [0] * n
        
        def dfs(k, idx, curSum):
            if k == 1:
                return True
            if curSum == target:
                # 试探curSum成功了，就 k -= 1， 继续搜索，visited来查重
                return dfs(k - 1, 0, 0)
            
            for i in range(idx, n): # start from idx because above will restart k - 1 from idx 0
                # 每次都试探把curSum 加到target
                if visited[i] == 0 and curSum + nums[i] <= target:
                    visited[i] = 1
                    if dfs(k, i + 1, curSum + nums[i]):  #这里用的 i 不是 idx
                        return True
                    visited[i] = 0  # if the dfs trial fail, reset that idx back to 0
            return False            # if all trial fail--> no feasible partition method
                    
        
        return dfs(k, 0, 0)