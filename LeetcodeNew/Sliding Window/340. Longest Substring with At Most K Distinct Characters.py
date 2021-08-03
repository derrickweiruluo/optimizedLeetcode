class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        counter = collections.Counter()
        res, left, distinct_count = 0, 0, 0
        
        for idx, char in enumerate(s):
            if counter[char] == 0:
                distinct_count += 1
            counter[char] += 1
            while distinct_count > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    distinct_count -=1
                left += 1
            res = max(res, idx - left + 1)
            
        return res
