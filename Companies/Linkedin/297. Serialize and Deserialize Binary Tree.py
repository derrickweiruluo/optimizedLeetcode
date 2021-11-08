"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return ""
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
            res.append(str(node.val) if node else "#")
        return ",".join(res)
        

    def deserialize(self, data):
        if not data: return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if nodes[idx] is not "#":
                node.left = TreeNode(int(nodes[idx]))
                queue.append(node.left)
            idx += 1
            
            if nodes[idx] is not "#":
                node.right = TreeNode(int(nodes[idx]))
                queue.append(node.right)
            idx += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
