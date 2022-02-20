'''
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Input: s = "abab", p = "ab"
Output: [0,1,2]
'''



class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p): return []
        
        res = []
        pCounter = collections.Counter(p)
        sCounter = collections.Counter()
        anagram_len = len(p)
        
        for i in range(len(s)):
            sCounter[s[i]] += 1
            if i >= anagram_len: 
                if sCounter[s[i - anagram_len]] == 1:
                    del sCounter[s[i - anagram_len]]
                else:
                    sCounter[s[i - anagram_len]] -= 1
            
            if pCounter == sCounter:
                res.append(i - anagram_len + 1)
        
        return res