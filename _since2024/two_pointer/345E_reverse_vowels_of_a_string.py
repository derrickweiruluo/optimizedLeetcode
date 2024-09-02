"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        i, j = 0, len(s) - 1
        res = list(s)
        while i < j:
            while s[i] not in vowels and i < j:
                i += 1
            while s[j] not in vowels and i < j:
                j -= 1
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        
        return "".join(res)