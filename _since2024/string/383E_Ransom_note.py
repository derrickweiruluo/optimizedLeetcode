from collections import defaultdict


class Solution:
    """
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
    by using the letters from magazine and false otherwise.
    Each letter in magazine can only be used once in ransomNote.

    Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

    Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

    Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = defaultdict(int)
        for char in magazine:
            char_count[char] += 1
        for char in ransomNote:
            if char_count[char] < 1:
                return False
            char_count[char] -= 1
        return True
