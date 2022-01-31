'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

'''



# Clarifications:
# All characters in words[i] and order are English lowercase letters.


# corner case:
# "apple", "appl" is False
# "hello", "hello", duplicate word is True
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        charOrder = {}
        for idx, char in enumerate(order):
            charOrder[char] = idx
        
        for i in range(1, len(words)):
            if self.isGreater(words[i - 1], words[i], charOrder):
                return False
        
        return True
    
    def isGreater(self, word1, word2, charOrder):
        m, n = len(word1), len(word2)
        for i in range(min(m, n)):
            if word1[i] != word2[i]:
                # that is, once found the first un-equal, early return of greater
                return charOrder[word1[i]] > charOrder[word2[i]]
        
        return m > n
        # corner case of abcd, abc. abcd is greater than abc, 
        # thus final length check