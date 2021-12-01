

class Solution:  # 68. Text Justification
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res, cur, charCount = [], [], 0
        
        for word in words:
            if charCount + len(cur) + len(word) > maxWidth:    # cur char count + len of possible spacing, len(cur) + len(next_word)
                for i in range(maxWidth - charCount):          # available spots remained
                    cur[i % (len(cur) - 1 or 1)] += " "         # (len - 1 or 1), 1 is for len == 0 so only cur[0] += space
            
                res.append("".join(cur))                        # a line of record
                cur, charCount = [], 0                         # reset cur, count for next line
            cur += [word]
            charCount += len(word)
        
        res += [" ".join(cur).ljust(maxWidth, " ")]             # add the last cur with ljust to res
        
        return res