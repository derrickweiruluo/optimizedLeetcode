'''
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]

'''

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        mapping = collections.defaultdict(list)
        
        for s in strings:
            key = self._hash(s)
            mapping[key].append(s)
        
        print(mapping)
        return mapping.values()
    
    def _hash(self, s):
        key = []
        for i in range(len(s) - 1):
            diff = (ord(s[i + 1]) - ord(s[i])) % 26
            key.append(str(diff))
        
        return '#'.join(key)