"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 
Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 
Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50

"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        left = res = 0
        counter = collections.Counter()
        
        for i, char in enumerate(s):
            counter[char] += 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            res = max(res, i - left + 1)
        
        return res
