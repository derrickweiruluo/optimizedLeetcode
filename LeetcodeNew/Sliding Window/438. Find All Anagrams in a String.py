class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        anagram_len = len(p)
        res = []
        
        p_count = collections.Counter(p)
        s_count = collections.Counter()
        
        for i in range(len(s)):
            s_count[s[i]] += 1
            if i >= anagram_len:   # sliding window
                if s_count[s[i - anagram_len]] == 1:
                    del s_count[s[i - anagram_len]]    # 减到0就要删除，不然下一步比较不出来
                else:
                    s_count[s[i - anagram_len]] -= 1   # count -= 1 for exisiting key:count

            if s_count == p_count:   # compare curr window to target
                res.append(i - anagram_len + 1)
        
        return res
                    
        
        
