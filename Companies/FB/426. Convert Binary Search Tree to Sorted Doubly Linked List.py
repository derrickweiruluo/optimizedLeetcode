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
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root: return None
        
        def inorder(node):
            head, tail = node, node
            if node.left:
                leftHead, leftTail = inorder(node.left)
                node.left = leftTail
                leftTail.right = node
                head = leftHead
            
            if node.right:
                rightHead, rightTail = inorder(node.right)
                node.right = rightHead
                rightHead.left = node
                tail = rightTail
            
            return head, tail # return lower bound and upper bound of a local root
        
        head, tail = inorder(root)
        tail.right, head.left = head, tail
        return head