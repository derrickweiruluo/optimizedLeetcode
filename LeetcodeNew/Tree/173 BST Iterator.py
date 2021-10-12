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

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []

    def next(self) -> int:
        # 遍历左子树，直到找到最小(leaf), curr 跟着走 (中序遍历)
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        node = self.stack.pop()
        self.cur = node.right
        return node.val

    def hasNext(self) -> bool:
        '''
        1. 在leaf node，curr会指向null，所以len != 0 是解
        2. 只要不在left node， 那一定有左右子树，所有有解
        3. 当在left 且 stack 也空，到了最大(最后)的一个节点，False'''
        return self.cur or len(self.stack)