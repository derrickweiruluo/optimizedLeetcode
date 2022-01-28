'''
The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.
'''

 #BEST
class Solution:
    def diameter(self, root: 'Node') -> int:
        
        self.depth = 0
        
        def dfs(node):
            if not node:
                return 0
            first, second = 0, 0
            for child in node.children:
                cur = dfs(child)
                if cur > first:
                    first, second = cur, first
                elif cur > second:
                    second = cur
            res = 1 + first + second

            self.depth = max(self.depth, res)
            return 1 + first
            
        
        dfs(root)
        return self.depth - 1



#### Bad solution
class Solution:
    def diameter(self, root: 'Node') -> int:
        self.maxPath = 0
        
        def dfs(root):
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
            self.maxPath = max(self.maxPath, cur)
            return 1 + lst[0]
        
        dfs(root)
        return self.maxPath