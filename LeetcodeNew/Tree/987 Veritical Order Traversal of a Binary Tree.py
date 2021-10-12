'''
二叉树的垂直traveral， 根据horizontal position来归类

        3
      /   \
     9     20
           / \
          15  7
Output: [[9],[3,15],[20],[7]]
'''

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque([(root, 0, 0)])
        mapping = collections.defaultdict(list)  # {column ID: listOfNodeVal}
        
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