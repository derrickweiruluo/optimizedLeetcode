"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

"""
import collections

class Solution:  # Both O(N), 最优解
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue = collections.deque([(root, 0)])
        mapping = collections.defaultdict(list)
        # 因为left right边界是由范围的，BFS记录范围，最后就用sort dict了
        left, right = math.inf, -math.inf
        
        
        while queue:
            for _ in range(len(queue)):
                node, col = queue.popleft()
                mapping[col].append(node.val)
                left = min(left, col)
                right = max(right, col)
                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))
        
        return [mapping[i] for i in range(left, right + 1)]



class Solution:  #DFS  time: W * H log H, space O(N)
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        self.left, self.right = math.inf, -math.inf

        def DFS(node, row, column):
            if node is not None:
                columnTable[column].append((row, node.val))
                self.left = min(self.left, column)
                self.right = max(self.right, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        res = []
        for col in range(self.left, self.right + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            res.append(colVals)

        return res


