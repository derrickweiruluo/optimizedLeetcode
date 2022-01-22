'''
Input: root = [4,2,5,1,3]

Inorder 方式转换成双向链表
Output: [1,2,3,4,5]
'''

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        
        head = Node(-1)
        prev = head
        cur = root
        
        while cur:
            if not cur.left:
                # linking start here
                cur.left = prev
                prev.right = cur
                prev = cur
                # linking finish here
                cur = cur.right
            else:
                predecessor = cur.left
                while predecessor.right != cur and predecessor.right:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = cur
                    cur = cur.left
                
                else:
                    predecessor.right = None
                    # linking happen here
                    cur.left = prev
                    prev.right = cur
                    prev = cur
                    # linking finish here
                    cur = cur.right

        print(head.val)
        head.right.left = prev      # 头尾链接
        prev.right = head.right     # 尾头链接
        return head.right           # dummy.right
            
        return None




# *--------------------

'''
Step 1: Divide:
We divide tree into three parts: left subtree, root node, right subtree.
Convert left subtree into a circular doubly linked list as well as the right subtree.
Be careful. You have to make the root node become a circular doubly linked list.

Step 2: Conquer:
Firstly, connect left circular doubly linked list with the root circular doubly linked list.
Secondly, connect them with the right circular doubly linked list. Here we go!
'''

class Solution: # O(N) time and O(H) space for recursion
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: 
            return None
        
        # Step 1 divide and conquer until one node left
        leftTree = self.treeToDoublyList(root.left)
        rightTree = self.treeToDoublyList(root.right)
        
        root.left = root
        root.right = root
        # 先把 DDL_left 连接 root，再连接 DDL_right
        return self.connect(self.connect(leftTree, root), rightTree) # constant time
    
    def connect(self, node1, node2):
        # node1 is ALWAYS the min node of a sorted DDL
        
        if not node1: return node2
        if not node2: return node1
        tail1 = node1.left   # tail1 means maxNode in DDL1, derive from node1.left
        tail2 = node2.left   # tail2 means maxNode in DDL2, derive from node2.left
        
        # connect 2 DDL by building 4 new connections
        tail1.right = node2
        tail2.right = node1
        node2.left = tail1
        node1.left = tail2
        
        return node1 # node1 is ALWAYS the Min node of a sorted DDL, return for next connect




# *-------------------------

# O(N) time and O(depth) space, average log(N) space

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



# Iterative In order Traversal
class Solution2:  #Iterative
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        stack = []
        trav = root
        head = Node(None)
        prev = None
        # iterative in order traversal
        while trav or stack:
            while trav:
                stack.append(trav)
                trav = trav.left            
            trav = stack.pop()
            # grab a reference to the first node
            if not head.right: head.right = trav
            # pred, succ links
            if prev: prev.right, trav.left = trav, prev
            prev = trav
            trav = trav.right
        
        # make circular
        prev.right = head.right
        head.right.left = prev
    
        return head