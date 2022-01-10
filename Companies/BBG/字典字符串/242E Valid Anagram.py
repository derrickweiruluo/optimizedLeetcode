'''
nput: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
'''

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        unicodeCounter = [0] * 256
        for char in s:
            unicodeCounter[ord(char) - ord('a')] += 1
        
        for char in t:
            unicodeCounter[ord(char) - ord('a')] -= 1
            if unicodeCounter[ord(char) - ord('a')] < 0:
                return False
        
        return sum(unicodeCounter) == 0
        
        # s = 'abcdé😀♞{23@#'
        # for i in range(len(u)):
        #     print(ord(u[i]))
        
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        for char in t:
            if char not in hashmap:
                return False
            else:
                hashmap[char] -= 1
        
        for val in hashmap.values():
            if val != 0:
                return False
        
        return True