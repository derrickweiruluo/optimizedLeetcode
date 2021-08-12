"""
Logical Thinking
We usually utilize stack when we face problems related to parenthesis. And it's time to do with the elements lying in the stack if we meet ')'. In this case, the element we popped should be left child of the element on top of the stack if there is no left child yet, or else, it will be the right child.
Please note that if there is only one node, i.e., the root of the Binary Tree, then the element on top of the stack is the root. Or else, the pointer parent points to the root in the last.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        stack, num, root = [], "", None
        
        for idx, char in enumerate(s):
            if char == ")":
                stack.pop()
            elif char == "(":
                continue
            else:
                num += char
                if idx + 1 == len(s) or not (s[idx + 1].isdigit()):
                    cur_node, num = TreeNode(num), ""
                    if stack:
                        parent = stack[-1]
                        if parent.left:
                            parent.right = cur_node
                        else:
                            parent.left = cur_node
                    else:
                        root = cur_node
                    stack.append(cur_node)
        
        return root
