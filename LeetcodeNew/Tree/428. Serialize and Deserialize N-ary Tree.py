"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Serialize with preorder traversal where sentinel "#" indicates the final child of a node has been processed, so the function returns to its parent call.
# Deserialize by creating a deque (could also use an iterator with next() instead of popleft()).
# While the next item is not "#", create a child with the item, add the child to the list of children and recurse to create its subtree.
# Repeat until there are no more children, then ignore the "#".

"""
We should return its level order traversal:
[
     [1],
     [3,2,4],
     [5,6]
]
The solution maintains the array for each level.
for _ in range(len(q)) means the number of nodes in each level,
and this loop finds all the children which belong to this level.
For example, you may serialize the following 3-ary tree
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
https://github.com/Taoge123/OptimizedLeetcode/blob/master/LeetcodeNew/Tree/LC_429_N_ary_Tree_Level_Order_Traversal.py

O(N) for both
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        
        if not root: return
        
        res = []
        def preorder(node):
            if not node: return
            res.append(str(node.val))
            for child in node.children:
                preorder(child)
            res.append('#')   # mark at the end of each leaf node
        
        preorder(root)
        return ','.join(res)
        
	
    def deserialize(self, data: str) -> 'Node':
        
        if not data: return
        
        queue = collections.deque(data.split(','))
        root = Node(int(queue.popleft()), [])
        
        def buildTree(node):
            if not node: return
            while queue[0] != '#':
                val = int(queue.popleft())
                child = Node(val, [])
                node.children.append(child)
                buildTree(child)
            if queue[0] == '#':
                queue.popleft()
        
        buildTree(root)
        return root
