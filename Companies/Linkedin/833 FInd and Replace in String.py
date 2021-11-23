'''
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].


Example 1:

Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
'''

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        replacement = zip(sources, indices, targets)
        res = list(s)                               # initialize the string as a char array
        
        for source, idx, target in replacement:     # zip the parallel array
            if s[idx: idx + len(source)] == source: # if repalcement condition match
                res[idx] = target                   # swap the first idx of res to target
                for i in range(idx + 1, idx + len(source)):
                    res[i] = ''                     # for res[idx + 1: idx + len], delete those old char
        
        return ''.join(res)