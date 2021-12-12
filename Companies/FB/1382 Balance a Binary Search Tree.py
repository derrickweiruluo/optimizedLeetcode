'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  # O(1) space
    def balanceBST(self, root: TreeNode) -> TreeNode:
        grand = TreeNode()
        grand.right = root
        count = self.makeVine(grand)
        height = int(log2(count + 1))
        remaining_nodes = pow(2, height) - 1
        self.compress(grand, count - remaining_nodes)
        while remaining_nodes > 0:
            remaining_nodes /= 2
            self.compress(grand, remaining_nodes)
        return grand.right
    
    def makeVine(self, grand, count = 0):
        node = grand.right
        while node:
            if node.left:
                old_node = node
                node = node.left
                old_node.left = node.right
                node.right = old_node
                grand.right = node
            else:
                count += 1
                grand = node
                node = node.right
        return count
    
    def compress(self, grand, m):
        node = grand.right
        while m > 1:
            m -= 1
            old_node = node
            node = node.right
            grand.right = node
            old_node.right = node.left
            node.left = old_node
            grand = node
            node = node.right



class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorderTraverse(node):
            if not node:
                return
            inorderTraverse(node.left)
            sortedNodes.append(node)
            inorderTraverse(node.right)
        
        def buildBST(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = sortedNodes[mid]
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root
        
        
        sortedNodes = []
        inorderTraverse(root)
        return buildBST(0, len(sortedNodes) - 1)