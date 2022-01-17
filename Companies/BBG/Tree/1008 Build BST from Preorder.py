'''
给一个BST preorder travesal的数组，返回该BST

'''

# Solution LEE
# Give the function a bound the maximum number it will handle.
# The left recursion will take the elements smaller than node.val
# The right recursion will take the remaining elements smaller than bound

# Complexity
# Time O(N)  Space O(H)
class Solution: # LEE
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        # buildTree is called exactly N times.
        # It's same as a preorder traversal.
        def buildBST(nums, upperBound):
            if not nums or nums[-1] >= upperBound:
                return None
            node = TreeNode(nums.pop())
            node.left = buildBST(nums, node.val)
            node.right = buildBST(nums, upperBound)
            return node
        
        
        # [8,5,1,7,10,12] -> [12,10,7,1,5,8]
        return buildBST(preorder[::-1], math.inf)



class Solution:  # same as sol1, just convert the input to deque first
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def buildBST(nums, upperBound):
            if not nums or nums[0] >= upperBound:
                return None
            node = TreeNode(nums.popleft())
            node.left = buildBST(nums, node.val)
            node.right = buildBST(nums, upperBound)
            return node
        
        # [8,5,1,7,10,12] -> [12,10,7,1,5,8]
        return buildBST(deque(preorder), math.inf)





"""
Idea is simple.
First item in preorder list is the root to be considered.
For next item in preorder list, there are 2 cases to consider:
If value is less than last item in stack, it is the left child of last item.
If value is greater than last item in stack, pop it.
The last popped item will be the parent and the item will be the right child of the parent.
"""


class Solution3:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root