'''
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)


'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.maxPath = 0
        
        def dfs(root): # Len of path = nums of node - 1
            if not root:
                return 0
            lst = []
            for child in root.children:
                h = dfs(child)
                lst.append(h)
            cur = 0
            lst.sort(reverse = True)
            if len(lst) == 1:
                cur += lst[0]
            elif len(lst) > 1:
                cur += (lst[0] + lst[1])
            else:
                self.maxPath = max(self.maxPath, 0)
                return 1
            self.maxPath = max(self.maxPath, cur) # 局部解
            return 1 + lst[0] # 递归给上一层的值
        
        dfs(root)
        return self.maxPath