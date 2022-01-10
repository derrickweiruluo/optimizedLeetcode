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

# ==>   "" + 3 * (a + 2 * c) == accaccacc

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        cnt = 0
        
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