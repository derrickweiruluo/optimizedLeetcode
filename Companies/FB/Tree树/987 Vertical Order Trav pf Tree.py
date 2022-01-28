'''
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

'''
import collections
s
class Solution:   # Best, only sort the value with the same indexes
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # required sorting order:
        # column, depth, value
        
        mapping = collections.defaultdict(lambda: defaultdict(list))
        left, right = math.inf, -math.inf
        up, down = math.inf, -math.inf
        queue = collections.deque([(root, 0, 0)])  # (node, col, depth)
        
        while queue:
            node, col, depth = queue.popleft()
            left, right = min(left, col), max(right, col)
            up, down = min(up, depth), max(down, depth)
            mapping[col][depth].append((node.val))
            if node.left:
                queue.append((node.left, col - 1, depth + 1))
            if node.right:
                queue.append((node.right, col + 1, depth + 1))
        
        res = []
        i = 0
        for col in range(left, right + 1):
            res.append([])
            for depth in range(up, down + 1):
                if depth in mapping[col]:
                    res[i].extend(val for val in sorted(mapping[col][depth]))
            i += 1
        
        return res


class Solution:  #BEST
    # 这个解包含BFS， DFS解法
    # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/777584/Python-Simple-dfs-explained

    '''  Complexity:  O(NlogN) and O(N)
    Time: Usual dfs traversal will take O(n) time. However we need to sort each level, before we give final result. Let us have w_1, ..., w_h nodes on each layer. then we need to do w_1 log w_1 + ... + w_h log w_h < n * log W operations, where W is width of the biggest layer. So, complexity is O(n log W), which potentially can be O(n log n), because the widest level can have upto n/2 nodes. 
    Space complexity is O(n).
    '''

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # queue = collections.deque([(root, 0, 0)])
        mapping = collections.defaultdict(list)  # {col: (depth, val)}
        self.left, self.right = math.inf, -math.inf
        res = []
        
        def dfs(node, col, depth):
            if not node: return
            self.left = min(self.left, col)
            self.right = max(self.right, col)
            mapping[col].append((depth, node.val))
            dfs(node.left, col - 1, depth + 1)
            dfs(node.right, col + 1, depth + 1)
        
        dfs(root, 0, 0)  # root at col 0, depth 0

        for i in range(self.left, self.right + 1):              # by col
            res += [[val for depth, val in sorted(mapping[i])]]   # by depth, then by value
        
        return res






class Solution:   # Best, only sort the value with the same indexes
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # required sorting order:
        # column, depth, value
        
        mapping = collections.defaultdict(lambda: defaultdict(list))
        left, right = math.inf, -math.inf
        up, down = math.inf, -math.inf
        queue = collections.deque([(root, 0, 0)])  # (node, col, depth)
        
        while queue:
            node, col, depth = queue.popleft()
            left, right = min(left, col), max(right, col)
            up, down = min(up, depth), max(down, depth)
            mapping[col][depth].append((node.val))
            if node.left:
                queue.append((node.left, col - 1, depth + 1))
            if node.right:
                queue.append((node.right, col + 1, depth + 1))
        
        res = []
        i = 0
        for col in range(left, right + 1):
            res.append([])
            for depth in range(up, down + 1):
                if depth in mapping[col]:
                    res[i].extend(val for val in sorted(mapping[col][depth]))
            i += 1
        
        return res