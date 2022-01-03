'''
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        k = 0
        
        for char in s:
            if char == '[':
                stack.append((cur_str, k))
                cur_str = ''
                k = 0
                
            elif char == ']':
                prev_str, prev_k = stack.pop()
                cur_str = prev_str + prev_k * cur_str
                
            elif char.isdigit():
                k = k * 10 + int(char)
                
            else: # just characters
                cur_str += char
            
        return cur_str