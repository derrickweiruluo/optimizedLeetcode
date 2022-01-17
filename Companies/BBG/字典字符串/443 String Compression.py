'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.


Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: 'a2b2c3'

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: "ab12".
'''

# follow up, count == 1 也要写出来


class Solution:  #O(1), modified in place
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        if n == 1: return n
        
        uniqueIdx, writeIdx = 0, 0
        
        for i in range(len(chars)):
            if i + 1 == n or chars[i] != chars[i + 1]:
                chars[writeIdx] = chars[i]
                writeIdx += 1
                
                if i > uniqueIdx:
                    repeatTimes = i - uniqueIdx + 1
                    for digit in str(repeatTimes):
                        chars[writeIdx] = digit
                        writeIdx += 1
                
                uniqueIdx = i + 1
        
        return writeIdx


###s
class Solution:  #O(1), modified in place
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        if n == 1: return n
        
        uniqueIdx, writeIdx = 0, 0
        
        for i in range(len(chars)):
            if i + 1 == n or chars[i] != chars[i + 1]:
                chars[writeIdx] = chars[i]
                writeIdx += 1
                
                if i >= uniqueIdx:
                    repeatTimes = i - uniqueIdx + 1
                    for digit in str(repeatTimes):
                        chars[writeIdx] = digit
                        writeIdx += 1
                
                uniqueIdx = i + 1
        
        return writeIdx

