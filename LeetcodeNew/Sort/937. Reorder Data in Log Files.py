"""
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.


Constraints:

1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.

"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        """split用法： 
        1. string.split()[idx:], which is the letter log to be sorted
        2. string.split()[1], 来测split完之后，idx_1 是 isdigit or isalpha 来分类"""
        
        digit_log = []
        letter_log = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)
        
        letter_log.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letter_log + digit_log
