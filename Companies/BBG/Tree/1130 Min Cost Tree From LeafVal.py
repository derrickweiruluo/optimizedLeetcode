
# [6,2,4,7]
#         42
#       /    \
#      24     7
#     /  \
#    6   8
#       / \
#      2   4



class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # [6,2,4,13,15,10,8,9,5,4,3,2]
        # [6,2,4,7]
        
        res = 0
        stack = [math.inf]  # non-increasing stack
        for i in range(len(arr)):
            while stack[-1] <= arr[i]:
                mid = stack.pop()
                res += mid * min(stack[-1], arr[i])  # construct and summing non-leaf nodes, next-greater 
            stack.append(arr[i])
        
        for i in range(2, len(stack)):              # construct and summing left over non-leaf nodes
            res += stack[i - 1] * stack[i]
        
        return res