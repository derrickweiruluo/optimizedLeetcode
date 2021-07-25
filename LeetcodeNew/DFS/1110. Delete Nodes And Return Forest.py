# Explanation
# If a node is root (has no parent) and isn't deleted,
# when will we add it to the result.

# if (is_root && !deleted) res.add(node)
# is_root: The node's parent is deleted. The node is the root node of the tree in the forest.
# !deleted: The node is not in the to_delete array.
# We only need to add the root node of every tree.


# Complexity
# Time O(N)
# Space O(H + N), where H is the height of tree.

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
