# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.


'''
Ex 1
        5
      /   \
    1      2
   / \    / \ 
  33  5  66  4


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 33 → 1 → 5 → 2 → 66.


Ex2:
        2
      /   
     1 

Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
'''


# Clarifications:
# 1.  All the values in the tree are unique.
# 2.  start, dest values are ALWAYS valid
# 3.  start != dest

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def getLCA(node):
            if not node:
                return node
            if node.val in (startValue, destValue):
                return node
            left = getLCA(node.left)
            right = getLCA(node.right)
            
            if left and right:
                return node
            else:
                return left or right
            
        LCA = getLCA(root)
        pathUp, pathDown = "", ""
        
        queue = collections.deque([(LCA, "")])
        while queue:
            node, path = queue.popleft()
            if node.val == startValue:
                pathUp = path
                if pathDown: break
            if node.val == destValue:
                pathDown = path
                if pathUp: break
            if node.left:
                queue.append((node.left, path + 'L'))
            if node.right:
                queue.append((node.right, path + 'R'))
        
        return 'U' * len(pathUp) + pathDown