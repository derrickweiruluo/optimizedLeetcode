'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # O(NK) time and space
        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return res.values()
        
        
        
        # Below is the NKlogK solution
        anagrams = collections.defaultdict(list)
        
        for string in strs:
            key = ''.join(sorted(string))
            anagrams[key].append(string)
        
        # print(list(anagrams.keys()))
        # print(list(anagrams.values()))
        return anagrams.values()