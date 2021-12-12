'''
You are given a string s and an array of strings words. You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words. If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag. If two substrings wrapped by bold tags are consecutive, you should combine them.

Example 1:

Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"
Example 2:

Input: s = "aaabbcc", words = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"
'''

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        n = len(s)
        status = [False] * n
        for word in words:
            start = s.find(word)
            length = len(word)
            while start != -1:
                for i in range(start, start + length):
                    status[i] = True
                start = s.find(word, start + 1)
        
        res = ""
        i = 0
        
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

'''
Here are two key points:

1. Trie Tree is used to speed up string match (faster than find or startwith in large query request).
2. Using Merge Intervals instead of mask to reduce Time and Space Complexity, both from O(n) to O(m), m represets interval numbers after merged.
'''

class Solution:
    def addBoldTag(self, s: str, dict: 'List[str]') -> str:
        trie = {}
        n = len(s)
        intervals = []
        res = ""

        # create trie tree
        for w in dict:
            cur = trie
            for c in w:
                cur = cur.setdefault(c, {})
            cur["#"] = 1

        # interval merge
        def add_interval(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                if intervals[-1][1] < interval[1]:
                    intervals[-1][1] = interval[1]
            else:
                intervals.append(interval)

        # make max match and add to interval
        for i in range(n):
            cur, max_end = trie, None
            for j in range(i, n):
                if s[j] not in cur:
                    break
                cur = cur[s[j]]
                if "#" in cur:
                    max_end = j + 1
            # just need to add max-match interval
            if max_end:
                add_interval([i, max_end])

        # concat result
        res, prev_end = "", 0
        for start, end in intervals:
            res += s[prev_end:start] + '<b>' + s[start:end] + "</b>"
            prev_end = end
        return res + s[prev_end:]