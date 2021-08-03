class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_char_count, res = 0, 0
        counter = collections.Counter()
        
        for idx, char in enumerate(s):
            counter[char] += 1
            max_char_count = max(max_char_count, counter[char])
            
            if res < max_char_count + k:
                res += 1
            else:
                # equivalent to move the left pointer by descreasing the leftmost counter by 1
                counter[s[idx - res]] -= 1
        
        return res
