'''
找一个longest的向下的 consecutive increasing path
The longest consecutive path needs to be 
from parent to child (cannot be the reverse).
'''

"""
Example 1:
Input:
   1
    \
     3
    / \
   2   4
        \
         5
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:
Input:
   2
    \
     3
    /
   2
  /
 1
Output: 2
"""

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        stack = collections.deque([(root, 1)])
        res = 0
        
        while stack:
            node, cnt = stack.popleft()
            if node.left:
                if node.left.val == node.val + 1:
                    stack.append((node.left, cnt + 1))
                else:
                    stack.append((node.left, 1))
            if node.right:
                if node.right.val == node.val + 1:
                    stack.append((node.right, cnt + 1))
                else:
                    stack.append((node.right, 1))
            res = max(res, cnt)
        
        return res



class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        def dfs(node, cnt, prev):
            if not node:
                return cnt
            if node.val - prev == 1:
                cnt += 1
            else:
                cnt = 1

            #DFS到下一层的时候，要知道 cnt值来判断是否连续，不连续 就 传下 cnt = 1
            left = dfs(node.left, cnt, node.val)
            right = dfs(node.right, cnt, node.val)
            return max(cnt, left, right)
        
        return dfs(root, 1, root.val)