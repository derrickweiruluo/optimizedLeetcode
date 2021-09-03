"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.

 
Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        left = res = 0
        counter = collections.Counter()
        
        for i, char in enumerate(s):
            counter[char] += 1
            
            while len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            res = max(res, i - left + 1)
        
        return res
