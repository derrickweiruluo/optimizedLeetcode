'''
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

'''
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution: # BFS-BEST  O(N), O(N)
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        mapping = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        left, right = math.inf, -math.inf
        res = []
        
        while queue:
            for _ in range(len(queue)):
                node, col, depth = queue.popleft()
                mapping[col].append((depth, node.val))
                left = min(left, col)
                right = max(right, col)
                if node.left:
                    queue.append((node.left, col - 1, depth + 1))
                if node.right:
                    queue.append((node.right, col + 1, depth + 1))
        
        # res = []
        # for i in range(left, right + 1):
        #     res += [[val for depth, val in sorted(mapping[i])]]
        # return res
        
        return [[val for depth, val in sorted(mapping[i])] for i in range(left, right + 1)]



class Solution:  #BEST
    # 这个解包含BFS， DFS解法

    # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/777584/Python-Simple-dfs-explained

    '''  Complexity:  O(NlogN) and O(N)
    Time: Usual dfs traversal will take O(n) time. However we need to sort each level, before we give final result. Let us have w_1, ..., w_h nodes on each layer. then we need to do w_1 log w_1 + ... + w_h log w_h < n * log W operations, where W is width of the biggest layer. So, complexity is O(n log W), which potentially can be O(n log n), because the widest level can have upto n/2 nodes. 
    Space complexity is O(n).
    '''

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # queue = collections.deque([(root, 0, 0)])
        mapping = collections.defaultdict(list)  # {col: (listOfNodeVal, depth)}
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






