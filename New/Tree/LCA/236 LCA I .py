"""
公共祖先
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

 


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

class Solution: # faster time with parent pointers w/ early return
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(parentNode, node):
            if not node:
                return None
            parent[node] = parentNode
            dfs(node, node.left)
            dfs(node, node.right)

        parent = {root: None}  # 可以 BFS也可以DFS构图
        # dfs(None, root)
        # def dfs(parentNode, node):
        #     if not node:
        #         return
        #     parent[node] = parentNode
        #     dfs(node, node.left)
        #     dfs(node, node.right)
        
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)

        visited = set()
        while p:
            visited.add(p)
            p = parent[p]
        while q not in visited:
            visited.add(q)
            q = parent[q]
        
        return q




# ##思路：
# DFS, leave's info will pass recursively back
# to the upper level
# 两种情况, root 左右都有解，该root就是LCA
# 只有一边有解， 就把该解传上去，如果传到顶点还是只有一个解，then LCA 
# 因为另一个 target在 LCA的子树里面

# time O(N), worse case iterate the whole tree with no early return
# space O(H~N)
class Solution:  # recursive
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: return root
        if left: return left
        if right: return right



# time O(N), worse case iterate the whole tree with no early return
# space O(H) to O(N)

class Solution:  # iterative
    
    #3 Recursive
    # https://leetcode.com/submissions/detail/600409983/
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Iterative
        stack = [root]
        parent = {root: None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        visited = set()
        while p:
            visited.add(p)
            p = parent[p]
        while q and q not in visited:
            q = parent[q]
        
        return q