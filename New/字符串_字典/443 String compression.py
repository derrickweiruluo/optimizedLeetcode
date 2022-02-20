'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
'''

# follow up, count == 1 也要写出来

class Solution:
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