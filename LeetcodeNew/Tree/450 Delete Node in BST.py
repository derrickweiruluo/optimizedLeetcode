"""
Example:
root = [5,3,6,2,4,null,7]
key = 3
    5
   / \
  3   6
 / \   \
2   4   7
Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
    5
   / \
  4   6
 /     \
2       7
Another valid answer is [5,2,6,null,4,null,7].
    5
   / \
  2   6
   \   \
    4   7
Steps:
1. Recursively find the node that has the same value as the key, while setting the left/right nodes equal to the returned subtree
2. Once the node is found, have to handle the below 4 cases
    - node doesn't have left or right - return null
    - node only has left subtree- return the left subtree
    - node only has right subtree- return the right subtree
    - node has both left and right - find the minimum value in the right subtree, set that value to the currently found node, then recursively delete the minimum value in the right subtree
"""

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:  # three cases when root == val
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.left and root.right:    # root's replacement is in root.right's leftmost
                minRight = root.right       
                while minRight.left:
                    minRight = minRight.left
                root.val = minRight.val
                # after replacement, recursively call this function to delete the replacing node again
                root.right = self.deleteNode(root.right, minRight.val)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        # this function return the root after the deletion at certain level
        return root