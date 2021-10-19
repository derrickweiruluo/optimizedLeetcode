'''
Serialize the binary tree
Deserialize the binary tree

'''

class Codec:
    def serialize(self, root):
        if not root: return ''
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('#')
        return ','.join(res)
        
    def deserialize(self, data):
        if not data: return
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