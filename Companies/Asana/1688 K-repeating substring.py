'''
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.
'''

# Example 1:

# Input: sequence = "ababc", word = "ab"
# Output: 2
# Explanation: "abab" is a substring in "ababc".

# Example 2:

# Input: sequence = "ababc", word = "ba"
# Output: 1
# Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".

# Example 3:

# Input: sequence = "ababc", word = "ac"
# Output: 0
# Explanation: "ac" is not a substring in "ababc".



class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        # O(N) is KMP
        
        # N^2 Brute Force
        length = 0
        n = len(word)
        while length < int(len(sequence) // n) + 1:
            if word * (length + 1) in sequence:
                length += 1
            else:
                break
        
        return length