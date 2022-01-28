'''
Convert BT to LL in the following ways:

convert following preorder traversal
'''


# O(1) space 
# Explaination:
# So we maintain a pointer curr while going down the tree. If curr has a left child, we want to shift it to the right while preserving the order. This will be two step process.
# Create another pointer p to find the right most point in the left subtree. Then we shift the contents of curr.right into p.right. The tree which we have right now (stage 2 in image) if you notice, still gives the exact same preorder traversal. So now we just shift this to the right of curr.

# Move curr to the right and repeat.

# 图文解释 https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/1208004/Extremely-Intuitive-O(1)-Space-solution-with-Simple-explanation-Python




# Clarifications: !!!!pre-order traversal !!!!!!!

class Solution: # O(1)
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # O(1) Space
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            else:
                cur = cur.right



# *----------------
# O(H) Space

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.curr_tail = None
        
        def traverse(node):
            if not node:
                return              # backtracking step
            traverse(node.right)    # go all the way to the right
            traverse(node.left)     # when finish right, go the left
            
            node.right = self.curr_tail    # keep track of the tail pointer 
            node.left = None               # delete the left pointer
            self.curr_tail = node          # the global tail become the current node upon finishing right and left
        
        traverse(root)