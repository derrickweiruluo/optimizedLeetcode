'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

'''

# DSW Algo:
# https://csactor.blogspot.com/2018/08/dsw-day-stout-warren-algorithm-dsw.html
# https://leetcode.com/problems/balance-a-binary-search-tree/discuss/541785/C%2B%2BJava-with-picture-DSW-O(n)orO(1)

# Clarifications:
# 一次性求解，不是动态

# Algorithm

# 1.    Convert the initial tree into a vine. By doing right rotations, we flatten a tree into a 'linked list', where the head is the former leftmost node, and tail - former rightmost node.
# 2.    As you convert the tree into a vine, count the total number of nodes in cnt.
# 3.    Calculate the height of the closest perfectly balanced tree: h = log2(cnt + 1).
# 4.    Calculate the number of nodes in the closest perfectly balanced tree: m = pow(2, h) - 1.
# 5.    Left-rotate cnt - m nodes to cover up the excess of nodes.
# Note: you rotate the root node, then you rotate the right child of the new root node, and so on. In other words, left rotations are performed on every second node of the vine. See pictures below for the illustration.

# 6.    Left-rotate m / 2 nodes.
# 7.    Divide m by two and repeat the step above while m / 2 is greater than zero.



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


# recursion, Time O(N), Space O(logN) for recursion build Tree
# Total Space O(N), 因为扫两遍了

class Solution:  
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sortedNodes.append(node)
            inorder(node.right)
        
        def buildBST(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = sortedNodes[mid]
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root
        
        
        sortedNodes = []
        inorder(root)
        return buildBST(0, len(sortedNodes) - 1)