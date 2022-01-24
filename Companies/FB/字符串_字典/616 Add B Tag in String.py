'''
1.  You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words. 
2.  If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.
3.  If two substrings wrapped by bold tags are consecutive, you should combine them.

https://leetcode.com/problems/add-bold-tag-in-string/discuss/104248/Java-Solution-boolean-array
'''


# Input: s = "abcxyz123", words = ["abc","123"]
# Status: [True, True, True, False, False, False, True, True, True]
# Output: "<b>abc</b>xyz<b>123</b>"


# Input: s = "aaabbcc", words = ["aaa","aab","bc"]
# Status [True, True, True, True, True, True, False]
# Output: "<b>aaabbc</b>c"


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        # prep to create a "Status" list for each index
        n = len(s)
        status = [False] * n
        for word in words:
            start = s.find(word)
            length = len(word)
            while start != -1:
                for i in range(start, start + length):
                    status[i] = True
                start = s.find(word, start + 1)  # repeatedly turn status to True if there is any cur-word remained
                # until stop at, which is -1
        
        res = ""
        i = 0
        
        # idx does not advance when adding tags
        while i < len(s):
            if status[i]:
                res += "<b>"
                while i < len(s) and status[i]:
                    res += s[i]
                    i += 1
                res += "</b>"
            else:
                res += s[i]
                i += 1
        
        return res