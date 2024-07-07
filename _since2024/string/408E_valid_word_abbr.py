"""
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
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        word_length, abbr_length = len(word), len(abbr)

        while i < word_length and j < abbr_length:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif word[i] != abbr[j]:
                if abbr[j].isalpha():
                    return False
                if abbr[j].isdigit() and abbr[j] == "0":
                    return False
                j_next = j
                while j_next < abbr_length and abbr[j_next].isdigit():
                    j_next += 1
                i += int(abbr[j: j_next])
                j = j_next
        return i == word_length and j == abbr_length
