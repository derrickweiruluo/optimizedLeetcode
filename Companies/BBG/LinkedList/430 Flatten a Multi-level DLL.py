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
            while cur:
                nextNode = cur.next
                if not nextNode:
                    tail = cur      # 定义尾部
                if cur.child:
                    cur.next, cur.child.prev = cur.child, cur
                    child_tail = dfs(cur.child)
                    
                    # if there is next node, 
                    # put the sub-Flat-LL between cur and next_node
                    if nextNode:
                        nextNode.prev = child_tail
                    child_tail.next = nextNode
                    cur.child = None
                
                cur = cur.next
            return tail             # dfs return tail of the current node, which to be used by nextNode
                    
        
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



    