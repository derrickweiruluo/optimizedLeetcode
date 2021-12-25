# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        root, stack, num = None, [], ""
        # num 用str记录方便处理负数
        
        n = len(s)
        
        for idx, char in enumerate(s):
            if char == ')':
                stack.pop() # if not the last node, parent will be there
            elif char == '(':
                continue
            else:
                num += char
                if idx + 1 == n or not s[idx + 1].isdigit():
                    curNode = TreeNode(num)
                    num = ""
                    if stack:
                        parent = stack[-1]
                        if parent.left:
                            parent.right = curNode
                        else:
                            parent.left = curNode
                    else:
                        root = curNode
                    stack.append(curNode)
        
        return root