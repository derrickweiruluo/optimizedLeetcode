'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

'''


'''
All characters in words[i] and order are English lowercase letters.
"apple", "appl" is False
'''



class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        self.charOrder = {}
        for idx, char in enumerate(order):
            self.charOrder[char] = idx
            
        for i in range(1, len(words)):
            if self.isGreater(words[i - 1], words[i]):
                return False
        return True
    
    def isGreater(self, word1, word2):
        m, n = len(word1), len(word2)
        for i in range(min(n, m)):
            if word1[i] != word2[i]:
                return self.charOrder[word1[i]] > self.charOrder[word2[i]]
        
        return n < m