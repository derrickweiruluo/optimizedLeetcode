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


# Time: k * 2 ^ n
# Once the first subset is found, we go on to find the second, which would take 2^N operations roughly (because some numbers have been marked as visited).

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < k: return False
        if sum(nums) % k != 0: return False
        
        target = sum(nums) / k
        visited = [0] * n  # # store the used/notUsed status of nums' idx
        nums.sort(reverse = True)
        
        def dfs(k, index, currSum):
            if k == 1:
                return True
            if currSum == target:
                # 试探curSum成功了，就 k -= 1， 继续搜索，visited来查重
                return dfs(k - 1, 0, 0)
            
            for i in range(index, n): # start from idx because above will restart k - 1 from idx 0
                # 每次都试探把curSum 加到target
                if visited[i] == 0 and currSum + nums[i] <= target:
                    visited[i] = 1
                    if dfs(k, i + 1, currSum + nums[i]):
                        return True
                    visited[i] = 0  # if the dfs trial fail, reset that idx back to 0
            return False            # if all trial fail--> no feasible partition method
                    
        
        return dfs(k, 0, 0)