# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        
        def dfs(node):
            if not node: return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return " ".join(map(str, vals))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        queue = collections.deque(int(val) for val in data.split())
        def buildTree(lowerBound, upperBound):
            if queue and lowerBound < queue[0] < upperBound:
                curr_val = queue.popleft()
                node = TreeNode(curr_val)
                node.left = buildTree(lowerBound, curr_val)
                node.right = buildTree(curr_val, upperBound)
                return node
        
        return buildTree(-math.inf, math.inf)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
