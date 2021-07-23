class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        head = root
        
        while root and root.left:
            next_level = root.left
            
            while root: # stop when root.next is None
                root.left.next = root.right
                
                # such as 2's next is None, therfore when root.right = 3,
                # root = root.next = None, break the while loop, move to next level
                root.right.next = root.next.left if root.next else None  
                root = root.next                                         
            
            root = next_level
        
        return head
