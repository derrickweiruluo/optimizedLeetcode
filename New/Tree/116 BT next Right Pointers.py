'''
        1
      /   \
    2      3
   / \    / \ 
  4   5  6   7



        1 -> NULL
      /   \
    2 -----3 -> NULL
   / \    / \ 
  4---5---6--7 -> NULL
'''

# 完美二叉树 only
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