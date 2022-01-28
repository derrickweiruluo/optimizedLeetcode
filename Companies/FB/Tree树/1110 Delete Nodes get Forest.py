'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        delete_set = set(to_delete)
        res = []
        
        def traverse(node, hasParent):
            if not node:
                return None
            node_deleted = node.val in delete_set

            if hasParent and not node_deleted:
                res.append(node)

            node.left = traverse(node.left, node_deleted)
            node.right = traverse(node.right, node_deleted)
            return None if node_deleted else node
            
        
        # Ask if root can be deleted, in here is no
        traverse(root, True)
        return res



class Solution:  #BFS
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        queue = collections.deque([(root, False)])
        res = []
        delete_set = set(to_delete)
        
        while queue:
            node, hasParent = queue.popleft()
            if not hasParent and node.val not in delete_set:
                res.append(node)
                
            hasParent = True
            if node.val in delete_set:
                hasParent = False
            
            if node.left:
                queue.append((node.left, hasParent))
                if node.left.val in delete_set:
                    node.left = None
            
            if node.right:
                queue.append((node.right, hasParent))
                if node.right.val in delete_set:
                    node.right = None
        
        return res