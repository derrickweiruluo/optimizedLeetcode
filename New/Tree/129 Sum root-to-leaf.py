''' 如题
sum of all root-to-leave numbers
'''


#         4
#       /   \
#     9       0
#   /   \   
# 5      1

# sum = 495 + 491 + 40 = 1026


# The idea of Morris algorithm is to set the temporary link between the node and its predecessor: predecessor.right = root. So one starts from the node, computes its predecessor and verifies if the link is present.

    # There is no link? Set it and go to the left subtree.
    # There is a link? Break it and go to the right subtree.

# There is one small issue to deal with : what if there is no left child, i.e. there is no left subtree? Then go straightforward to the right subtree.



class Solution:  # Morris, O(1) Space
    def sumNumbers(self, root: TreeNode):
        res = curVal = 0
        
        while root:
            # If there is no left child
            # then just go right.        
            if not root.left:
                curVal = curVal * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    res += curVal
                root = root.right

            else: 
                predecessor = root.left 
                steps = 1
                while predecessor.right and predecessor.right is not root: 
                    predecessor = predecessor.right 
                    steps += 1

                if predecessor.right is None: # first visit
                    curVal = curVal * 10 + root.val                    
                    predecessor.right = root  
                    root = root.left  

                else: # second visit
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        res += curVal
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curVal //= 10
                    predecessor.right = None
                    root = root.right 


class Solution:  # Space O(w)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([(root, 0)])
        res = 0
        
        while queue:
            node, curVal = queue.popleft()
            curVal = curVal * 10 + node.val
            if not node.left and not node.right:
                res += curVal
            if node.left:
                queue.append((node.left, curVal))
            if node.right:
                queue.append((node.right, curVal))
        
        return res


class Solution: # O(H) Space
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def dfs(node, prevSum):
            if not node:
                return 0
            curVal = prevSum * 10 + node.val

            if not node.left and not node.right:
                self.res += curVal
            dfs(node.left, curVal)
            dfs(node.right, curVal)
        
        dfs(root, 0)  # node, and the prevSum above this node
        return self.res


                    
            
                
                        
        return res