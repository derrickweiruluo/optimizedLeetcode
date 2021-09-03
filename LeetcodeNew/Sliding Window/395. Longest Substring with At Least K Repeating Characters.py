"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 
Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 
Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if len(s) < k:
            return 0
        min_freq_char = min(s, key = s.count)
        if s.count(min_freq_char) >= k:
            return len(s)
        return max(self.longestSubstring(seq, k) for seq in s.split(min_freq_char))