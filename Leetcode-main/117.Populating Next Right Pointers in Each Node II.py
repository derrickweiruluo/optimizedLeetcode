"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        
        while root:
            curr_node = dummy = Node(0)
            
            while root:
                if root.left:
                    curr_node.next = root.left
                    curr_node = curr_node.next
                if root.right:
                    curr_node.next = root.right
                    curr_node = curr_node.next
                    
                root = root.next
            
            root = dummy.next
        
        return head
