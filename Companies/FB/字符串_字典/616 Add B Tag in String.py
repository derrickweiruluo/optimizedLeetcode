'''
1.  You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words. 
2.  If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.
3.  If two substrings wrapped by bold tags are consecutive, you should combine them.

https://leetcode.com/problems/add-bold-tag-in-string/discuss/104248/Java-Solution-boolean-array
'''




# Input: s = "aaabbcc", words = ["aaa","aab","bc"]
# Status [True, True, True, True, True, True, False]
# Output: "<b>aaabbc</b>c"



class Solution:  # Trie 优化解
    def addBoldTag(self, s: str, words: List[str]) -> str:

        # _trie = lambda: collections.defaultdict(_trie)
        trie = {}
        
        for w in words:
            cur = trie
            for c in w:
                cur = cur.setdefault(c, {})
            cur["#"] = 1

        
        # 步骤和下面的解一样，多了trie步骤来 speed up status boolean array的构建
        status = [False] * len(s)
        for i in range(len(s)):
            cur = trie
            end = i
            for j in range(i, len(s)):
                if s[j] not in cur: break
                cur = cur[s[j]]
                if "#" in cur:
                    end = j + 1
            status[i:end] = [True] * (end - i)
        
        ans = []
        for i, u in enumerate(s):
            if status[i] and (i == 0 or not status[i-1]):
                ans.append('<b>')
            ans.append(u)
            if status[i] and (i == len(s) - 1 or not status[i+1]):
                ans.append('</b>')
            
        return "".join(ans)




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