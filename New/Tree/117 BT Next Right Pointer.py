'''
        1
      /   \
    2      3
   / \      \ 
  4   5      7



        1 -> NULL
      /   \
    2 -----3 -> NULL
   / \      \ 
  4---5------7 -> NULL
'''



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        # prev 只在完成一层操作，给root指引到下一层的leftmost
        # prev 并且给child reset到初始zhuangtai prev == child == Node(0)
        # prev 永远不变的，是给root 降层和 child reset用
        prev = child = Node(0)
        
        
        cur = root
        while cur:
            # inner loop for 当前层的操作，目标是处理好，且update最左边的node pointer
            # 因为上一层的next 设置好了，等于可以用这个next pointer来跨越同一层的下一个node
            # 每一层的最后一个node -> Null 都是通过下一层的 root = root.next来实现
            # 最底层只会运行一个操作让最后一个node指向null
            while cur:  # iterate the level
                if cur.left:
                    child.next = cur.left
                    child = child.next
                if cur.right:
                    child.next = cur.right
                    child = child.next
                
                # build the next pointer for the next_level nodes
                # rightMost will just be None
                # and this will break in the inner-level while loop
                cur = cur.next  
            
            # print(prev.next.val, prev.val)
            cur, child = prev.next, prev
            child.next = None
        
        return root