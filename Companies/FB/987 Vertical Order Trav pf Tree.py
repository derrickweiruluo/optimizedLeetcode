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

class Solution:  #BEST
    # 这个解包含BFS， DFS解法

    # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/777584/Python-Simple-dfs-explained

    '''
    Complexity: 
    Time: Usual dfs traversal will take O(n) time. However we need to sort each level, before we give final result. Let us have w_1, ..., w_h nodes on each layer. then we need to do w_1 log w_1 + ... + w_h log w_h < n * log W operations, where W is width of the biggest layer. So, complexity is O(n log W), which potentially can be O(n log n), because the widest level can have upto n/2 nodes. 
    Space complexity is O(n).
    '''

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque([(root, 0, 0)])
        mapping = collections.defaultdict(list)  # {col: listOfNodeVal}
        self.left, self.right = math.inf, -math.inf
        
        # while queue:
        #     node, column, depth = queue.popleft()
        #     if not node:
        #         continue
        #     mapping[column].append((node.val, depth))
        #     self.left, self.right = min(self.left, column), max(self.right, column)
        #     queue.append((node.left, column - 1, depth + 1))
        #     queue.append((node.right, column + 1, depth + 1))
        
        def dfs(node, column, depth):
            self.left, self.right = min(self.left, column), max(self.right, column)
            mapping[column].append((node.val, depth))
            if node.left:  dfs(node.left,  column - 1, depth + 1)
            if node.right: dfs(node.right, column + 1, depth + 1)
        
        dfs(root, 0, 0)
        
        res = []
        for i in range(self.left, self.right + 1):
            res += [[val for val, col in sorted(mapping[i], key = lambda x: (x[1], x[0]))]]

        return res






class Solution: #Naive
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque([(root, 0, 0)])
        mapping = collections.defaultdict(list)  # {col: listOfNodeVal}
        
        while queue:
            node, column, depth = queue.popleft()
            if not node:
                continue
            mapping[column].append((node.val, depth))
            queue.append((node.left, column - 1, depth + 1))
            queue.append((node.right, column + 1, depth + 1))
        
        res = [[None]] * len(mapping)
        idx = 0
        for col, lst in sorted(mapping.items()):
            lst.sort(key = lambda x: (x[1], x[0]))
            res[idx] = [val for val, depth in lst]
            idx += 1

        return res