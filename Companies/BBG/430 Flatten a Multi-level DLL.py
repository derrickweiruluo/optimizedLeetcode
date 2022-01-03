### Clarifications and Requirements:

# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

# Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.




class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head: return
        dummy = prev = Node(0, None, head, None)
        stack = [head]
        
        while stack:
            curr = stack.pop()
            prev.next, curr.prev = curr, prev
            
            if curr.next:
                stack.append(curr.next)
                curr.next = None
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        
        dummy.next.prev = None
        return dummy.next


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head: return
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