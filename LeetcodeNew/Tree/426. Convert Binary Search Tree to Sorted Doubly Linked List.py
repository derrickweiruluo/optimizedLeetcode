'''
Input: root = [4,2,5,1,3]

Inorder 方式转换成双向链表
Output: [1,2,3,4,5]

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        if not root: return
        
        def inorder(node):
            head, tail = node, node
            if node.left:
                left_head, left_tail = inorder(node.left)
                node.left = left_tail
                left_tail.right = node
                head = left_head
                
            if node.right:
                right_head, right_tail = inorder(node.right)
                node.right = right_head
                right_head.left = node
                tail = right_tail
                
            return head, tail # return lower bound and upper bound of a local root
        
        head, tail = inorder(root)
        tail.right = head
        head.left = tail
        
        return head