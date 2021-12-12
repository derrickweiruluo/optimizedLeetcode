'''
Input: root = [4,2,5,1,3]

Inorder 方式转换成双向链表
Output: [1,2,3,4,5]

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

'''
This is not O(1) space. It is O(tree depth), so O(n) worst case and O(log(n)) average case.

Keep in mind that the recursive call stack takes space, and there will be (at maximum depth) one stack from for each level in the tree
'''

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