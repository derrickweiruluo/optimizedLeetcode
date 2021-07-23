class Solution:
  
#   space O(n)
#     def scoreOfParentheses(self, s: str) -> int:
#         res, level, n = 0, 0, len(s)
#         for i in range(n):
#             if s[i] == "(":
#                 level += 1
#             else:
#                 level -= 1
#                 if s[i - 1] == "(":
#                     res += 2 ** level
#         return res
        
#         ** O(n) ** version
        stack, cur = [], 0
        for i in s:
            if i == "(":
                stack.append(cur)
                cur = 0. # cur是stack最上方的累积值
            else:
                cur += stack.pop() + max(1, cur)  # 这一步相当于 cur * 2， 最里面那层的话就是 0 + max(1, 0) 
        
        return cur
