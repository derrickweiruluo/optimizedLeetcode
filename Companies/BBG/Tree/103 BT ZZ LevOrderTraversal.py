


# Time O(n), Space O(Width, n/2 worst case for perfect BT)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur)
            
        for i in range(len(res)):  # O(n)
            if i % 2 == 1:
                res[i] = res[i][::-1]
        
        return res



# DFS
class Solution(object):
    def zigzagLevelOrder(self, root):
        def dfs(node, level):
            while level >= len(res): res.append([])
            res[level] += [node.val]
            if node.left: dfs(node.left, level+1)
            if node.right: dfs(node.right, level+1)
            
        if not root: return []
        res = []
        dfs(root, 0)
        return [res[level] if not level % 2 else res[level][::-1] for level in range(len(res))]



# Similar to the 1st one
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = collections.deque([root])
        res = []
        reverse = -1
        
        while queue:
            cur = []
            for _ in range(len(queue)):
                if reverse == 1:
                    node = queue.popleft()
                    cur.append(node.val)
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                else:
                    node = queue.pop()
                    cur.append(node.val)
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)
            reverse *= -1        
            res.append(cur)
        
        return res