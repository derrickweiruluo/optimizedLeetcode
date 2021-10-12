'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation


1.  In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the intermediate result. Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
2.  This is a classical 'space and time tradeoff': we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency.
3.  Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
4.  We just need to add the frequency of the oldPathSum to the result.
5.  During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.
6.  Check the graph below for easy visualization.

O(n) space for dfs and cache, O(n) time
'''

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = collections.defaultdict(int)
        cache[0] = 1
        self.res = 0
        self.dfs(root, targetSum, 0, cache)
        return self.res
    
    def dfs(self, root, target, curSum, cache):
        if not root:
            return
        curSum += root.val
        self.res += cache[curSum - target]
        cache[curSum] += 1
        self.dfs(root.left, target, curSum, cache)
        self.dfs(root.right, target, curSum, cache)
        cache[curSum] -= 1