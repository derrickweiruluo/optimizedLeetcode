'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
'''

class BSTIterator:  # BEST with Morris Order 

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root

    def next(self) -> int:
        res = math.inf
        while self.cur:
            if not self.cur.left:
                res = self.cur.val
                self.cur = self.cur.right
                break
            else:
                predecessor = self.cur.left
                while predecessor.right != self.cur and predecessor.right:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = self.cur
                    self.cur = self.cur.left
                
                else:
                    predecessor.right = None
                    res = self.cur.val
                    self.cur = self.cur.right
                    break
        return res
                

    def hasNext(self) -> bool:
        return self.cur





class BSTIterator: # BEST_2, O(1) time average of N next call, O(H) space

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = root
    
    def next(self) -> int: #O(1) time 
        #   Think about the number of times a node has been visited after iterating the whole tree. Each node has been visited twice. In some cases the while loop doesn't execute, so that node at that call is only visited once. Where does the other visit go? It goes to the while loop when you visit another node. That's why it's "average" O(1) time.

        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        curVal = self.cur.val
        self.cur = self.cur.right
        return curVal
    
    def hasNext(self) -> bool:
        # at leaf node, stack is not null
        # when backtrack to root(sub-root), stack is empty but cur is not
        return self.stack or self.cur




class BSTIterator:  # Morris Order: O(1) for both

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = root
    
    def next(self) -> int:
        res = 0
        while self.cur:
            
            # step A
            if not self.cur.left:
                # do sth
                res = self.cur.val
                self.cur = self.cur.right
                break
                
            # step B
            else:
                predecessor = self.cur.left
                
                # step B1, find left-subtree's rightmost node, but not itself
                while predecessor.right != self.cur and predecessor.right:
                    predecessor = predecessor.right
                
                # step B2, build the temporary conn
                if not predecessor.right:  # 第一次还不存在 predeessor -> node link, build it, go left
                    predecessor.right = self.cur
                    self.cur = self.cur.left       # 继续走左道
                
                # step B3, remove the tempo conn
                else:  # 第2次visit, break the temp link of a node's predecesor
                    # do sth
                    res = self.cur.val
                    predecessor.right = None
                    self.cur = self.cur.right       # 开始探索柚子树
                    break
        
        return res
    
    def hasNext(self) -> bool:
        # at leaf node, stack is not null
        # when backtrack to root(sub-root), stack is empty but cur is not
        return self.cur





class BSTIterator:  # BEST

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, root): 
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:      #O(1)
        
        node = self.stack.pop()
        self.pushLeft(node.right)
        return node.val

    def hasNext(self) -> bool:  #O(1)
        return self.stack





class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []

    def next(self) -> int: # O(1)
        # 遍历左子树，直到找到最小(leaf), curr 跟着走 (中序遍历)
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        node = self.stack.pop()
        self.cur = node.right
        return node.val

    def hasNext(self) -> bool: # O(1)
        '''
        1. 在leaf node，curr会指向null，所以len != 0 是解
        2. 只要不在left node， 那一定有左右子树，所有有解
        3. 当在left 且 stack 也空，到了最大(最后)的一个节点，False'''
        return self.cur or len(self.stack)