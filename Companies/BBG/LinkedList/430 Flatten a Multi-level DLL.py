'''

    1 -- 2 -- 3 -- 4 -- 5
              |
              |
              7 -- 8 -- 9
                   |
                   |
                   11 -- 12



Flattened:

    1 -- 2 -- 3 -- (7,8,9,11,12) -- 4 -- 5
    
        (7,8,9,11,12) ==>  7 -- (8,11,12) -- 9

            (8,11,12)   ==>  8 -- 11 -- 12

    1 -- 2 -- 3 -- (7 -- (8 -- 11 -- 12) -- 9) -- 4 -- 5
'''



# Clarifications:
# child-sub-LL is between cur and cur.next.
# remove the child node, flatten to DLL
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head: return
        
        def dfs(curr):
        # recursive approach
            while curr:
                next_node = curr.next

                if not next_node:
                    tail = curr
                if curr.child:
                    curr.next, curr.child.prev = curr.child, curr
                    child_tail = dfs(curr.child)

                    # if there is next node, 
                    # put the sub-Flat-LL between cur and next_node
                    if next_node:
                        next_node.prev = child_tail
                    child_tail.next = next_node # if cur has no next_node, just point to null
                    curr.child = None

                curr = curr.next  
            return tail # return tail of the current node

        dfs(head)
        return head
    



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



    