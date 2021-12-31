# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




# Input: s = "4(2(3)(1))(6(5))"
# 优先填充左边

#         4
#       /   \
#     2       6
#    / \     /
#   3   1   5

# 一样的写法，只是先建立了 rootVal，比较适合interview，上面那个太精炼了
class Solution:  
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        rootVal = s.split('(')[0]
        
        if not rootVal: return None
        
        i = len(rootVal)
        root = TreeNode(rootVal)
        
        num = ""
        stack = [root]
        
        while i < len(s):
            if s[i] == '(':
                i += 1
                continue
            elif s[i] == ')':
                i += 1
                stack.pop()  # garanteed to be valid
            else:
                num += s[i]
                if i + 1 == len(s) or not s[i + 1].isdigit():
                    curNode = TreeNode(num)
                    num = ""
                    if stack:
                        parent = stack[-1]
                        if parent.left:  # 如果左边已经被填充了，就连接右边(题目要求从左到右连接孩子)
                            parent.right = curNode
                        else:            # 如果左边还没有被填充了，就连接先连边
                            parent.left = curNode
                    # 必走的一步
                    stack.append(curNode)
                i += 1
        return root





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
                        if parent.left:     # 如果左边已经被填充了，就连接右边(题目要求从左到右连接孩子)
                            parent.right = curNode
                        else:               # 如果左边还没有被填充了，就连接先连边
                            parent.left = curNode
                    else:
                        root = curNode
                    
                    # 必走的一步
                    stack.append(curNode)
        
        return root


