'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.


For example, a string such as "substitution" could be abbreviated as (but not limited to):


Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

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
                return False
            elif word[i] != abbr[j] and abbr[j].isdigit():
                if abbr[j] == '0':
                    return False # leading zero, invalid case
                elif abbr[j].isdigit():   # or just else is fine
                    k = j
                    while k < n and abbr[k].isdigit():
                        k += 1
                    i += int(abbr[j: k]) # index k not include since already non-digit
                    j = k
        
        # both pointers reach to the ends
        return i == m and j == n