'''
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # counter = collections.Counter(s)
        
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        
        res = 0
        for char in t:
            if char in counter and counter[char] > 0:
                counter[char] -= 1
                if counter[char] == 0:
                    counter.pop(char)
            else:
                res += 1
        
        return res