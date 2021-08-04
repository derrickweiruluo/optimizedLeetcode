"""

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",  
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
"""


class Solution1:  # 68. Text Justification
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res, cur, char_count = [], [], 0
        
        for idx, word in enumerate(words):
            if char_count + len(cur) + len(word) > maxWidth:    # cur char count + len of possible spacing, len(cur) + len(next_word)
                for i in range(maxWidth - char_count):          # available spots remained
                    cur[i % (len(cur) - 1 or 1)] += " "         # (len - 1 or 1), 1 is for len == 0 so only cur[0] += space
            
                res.append("".join(cur))                        # a line of record
                cur, char_count = [], 0                         # reset cur, count for next line
            cur += [word]
            char_count += len(word)
        
        res += [" ".join(cur).ljust(maxWidth, " ")]             # add the last cur with ljust to res
        
        return res


      
      
      
"""
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
