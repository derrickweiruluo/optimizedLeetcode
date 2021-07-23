"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head: return
        # iterative
#         dummy = prev = Node(0, None, head, None)
#         stack = [head]
        
#         while stack:
#             curr = stack.pop()
#             prev.next, curr.prev = curr, prev
            
#             if curr.next:
#                 stack.append(curr.next)
#                 curr.next = None
#             if curr.child:
#                 stack.append(curr.child)
#                 curr.child = None
#             prev = curr
        
#         dummy.next.prev = None
#         return dummy.next

        self.traverse(head)
        return head
    
    def traverse(self, curr):
        # recursive approach
        while curr:
            next_node = curr.next
            if not next_node:
                tail = curr
            if curr.child:
                curr.next, curr.child.prev = curr.child, curr
                child_tail = self.traverse(curr.child)
                if next_node:
                    next_node.prev = child_tail
                child_tail.next = next_node
                curr.child = None
            
            curr = curr.next  
        return tail # return tail of the current node
                
                
                
                
                
                
                
                
                
                
                
                
        
