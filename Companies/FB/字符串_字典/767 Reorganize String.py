'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
'''


# Time O(N): counter + find_max + write results into char array
# Space O(N + 26): result + hash[]

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = collections.Counter(s)
        n = len(s)
        
        maxKey = max(counter, key = counter.get)
        maxCount = counter[maxKey]
        if maxCount > (len(s) + 1) // 2:
            return ""
        
        res = [""] * n
        idx = 0
        
        # Step 1: Fill the most frequent char first
        for i in range(maxCount):
            res[idx] = maxKey
            idx += 2
        del counter[maxKey]
        
        if idx >= n: idx = 1 
        # step 2: iterate all other char-freq, and fill rest of the idx
        for letter, count in counter.items():
            for i in range(count):
                res[idx] = letter
                idx += 2
                if idx >= n:
                    idx = 1
        
        
        return "".join(res)