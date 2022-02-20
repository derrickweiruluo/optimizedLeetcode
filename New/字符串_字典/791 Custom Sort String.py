'''
You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.

 
Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
'''



# Time & Space: O(N), where N is length the string
# Time == order + s, s dominates usually
# Space is fix-size since only 26 keys
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        counter = collections.Counter(s)
        res = []
        
        for char in order:    # by ordering, construct the res
            if counter[char]:
                res += [char * counter.pop(char)]
                # res.append(char * counter.pop(char))
        
        for char in s:
            if char not in order:
                res += [char]
            
        return ''.join(res)