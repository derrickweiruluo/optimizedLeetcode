# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

lass Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        res = []
        
        def preorder(node):
            if not node: return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ' '.join(res)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        ## strick在于构建的时候如果
        
        vals = [int(val) for val in data.split()]
        queue = collections.deque(vals)
        def buildTree(lowerBound, upperBound):
            if not queue: return
            if queue and lowerBound < queue[0] < upperBound:
                curr_val = queue.popleft()
                node = TreeNode(curr_val)
                node.left = buildTree(lowerBound, curr_val)
                node.right = buildTree(curr_val, upperBound)
                return node
        
        return buildTree(-10001, 10001)
        
