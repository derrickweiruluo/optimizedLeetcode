'''
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''


# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# before reaching a, stack = [("", 3)]
# before reaching c, stack = [("", 3), ("a", 2)]

# when seeing first ]:      'a' + 2 * c, where stack.pop() get ('a', 2)
# when seeing sencond ]:    '' + 3 * ('acc'), where stack.pop() get ('', 3)

# ==>   "" + 3 * (a + 2 * c) == accaccacc

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        cnt = 0
        
        # stack to 储存 左括号左边的结果， 当第一个右括号出现，pop一次
        # 来更新当前层

        for char in s:
            if char.isdigit():
                cnt = cnt * 10 + int(char)
            elif char.isalpha():
                cur_str += char
            elif char == '[':
                stack.append((cur_str, cnt))
                cur_str = ''
                cnt = 0
                
            elif char == ']':
                prev_str, prev_cnt = stack.pop()
                cur_str = prev_str + prev_cnt * cur_str
                
            
        return cur_str



# DFS
class Solution(object):
    def decodeString(self, s):
        return helper(list(s)[::-1])

    def helper(s):
        res = ""
        while s:
            num = ""
            while s and s[-1] in '0123456789':
                num += s.pop()
            if num:
                num = int(num)
                s.pop()
                res += helper(s) * num
            else:
                c = s.pop()
                if c not in "[]":
                    res += c
                if c == ']':
                    break
        return res