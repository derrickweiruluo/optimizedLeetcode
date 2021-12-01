'''
IMO, time complexity = o(n) and space complexity=O(h), where h is the height of the tree (since it is recursive call, and needs stack space)

Yes, both time complexity and space complexity are O(n). Time complexity is O(n) since it has to traverse through all nodes. Space complexity is O(n) since the recursive stack may go up to n, in case the tree is completely skewed.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ''
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append('#')
        print(','.join(res))
        return ','.join(res)
        

    def deserialize(self, data):
        if not data: return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = collections.deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if data[idx] != '#':
                node.left = TreeNode(int(data[idx]))
                queue.append(node.left)
            idx += 1
            if data[idx] != '#':
                node.right = TreeNode(int(data[idx]))
                queue.append(node.right)
            idx += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
