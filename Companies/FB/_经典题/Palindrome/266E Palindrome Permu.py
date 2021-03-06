'''
Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.

'''

class Solution:  # BEST, One-Pass
    def canPermutePalindrome(self, s: str) -> bool:
        
        mapping = [0] * 256
        count = 0
        for char in s:
            idx = ord(char) - ord('a')
            mapping[idx] += 1
            if mapping[idx] % 2 == 0:
                count -= 1
            else:
                count += 1
        
        return count < 2




# Time: O(N), space O(26), or O(# of unique chars)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        
        res = 0
        # print(counter)
        for char, freq in counter.items():
            if freq % 2:
                res += 1
            if res > 1:
                return False
        
        return True



class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        charCounter = collections.Counter(s)
        
        return sum(val % 2 for val in charCounter.values()) <= 1