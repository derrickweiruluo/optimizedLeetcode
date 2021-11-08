'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


EX1: 
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]


EX2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
'''


class Solution:  # 68. Text Justification
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res, cur, char_count = [], [], 0
        
        for idx, word in enumerate(words):
            # cur char count + len of possible spacing, len(cur) + len(next_word)
            if char_count + len(cur) + len(word) > maxWidth:    
                for i in range(maxWidth - char_count):
                    # available spots remained          
                    cur[i % (len(cur) - 1 or 1)] += " " 
                    # (len - 1 or 1), 1 is for len == 0 so only cur[0] += space        
            
                res.append("".join(cur))       # a line of record
                cur, char_count = [], 0        # reset cur, count for next line
            cur += [word]
            char_count += len(word)
        
        # add the last cur with ljust to res
        res += [" ".join(cur).ljust(maxWidth, " ")] 
        
        
        return res