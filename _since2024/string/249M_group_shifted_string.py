"""
Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.


Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]
Output: [["a"]]
"""

import collections


class Solution_2024:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapping = collections.defaultdict(list)

        def convert_to_sequence_key(input_string):
            hash_key = ""
            for i in range(len(input_string) - 1):
                # convert to unicode-integer then do substration
                offset = (ord(input_string[i + 1]) - ord(input_string[i])) % 26
                hash_key += str(offset) + "_"
            return hash_key

        for s in strings:
            mapping[convert_to_sequence_key(s)].append(s)

        return mapping.values()









class Solution_2021:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        mapping = collections.defaultdict(list)
        
        def convert(s):
            hashKey = []
            for i in range(len(s) - 1):
                # clarification of warp around 
                # % 26 make 'AZ' same as 'BA' -> warp around
                diff = (ord(s[i + 1]) - ord(s[i])) % 26  
                hashKey.append(str(diff))
            return '#'.join(hashKey)
        
        for s in strings:
            mapping[convert(s)].append(s)
        
        # print(mapping)
        return mapping.values()  #return a list of string array