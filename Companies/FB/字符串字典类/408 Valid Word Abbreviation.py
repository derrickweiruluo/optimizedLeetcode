'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.


For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".

'''


### Clarification:
'''
word consists of only lowercase English letters.
abbr consists of lowercase English letters and digits.
Abbr could be invalid
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = j = 0
        m, n = len(word), len(abbr)
        
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif word[i] != abbr[j] and abbr[j].isalpha():
                # print(i, j)
                return False
            else:
                if abbr[j] == '0':
                    return False # leading zero, invalid case
                elif abbr[j].isdigit():
                    k = j
                    while k < n and abbr[k].isdigit():
                        k += 1
                    i += int(abbr[j: k]) # index k not include since already non-digit
                    j = k
        
        return i == m and j == n