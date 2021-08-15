"""
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 2, b = 2, c = 1
Output: "aabbc"

Example 3:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 

Constraints:
0 <= a, b, c <= 100
a + b + c > 0

#################
The algorithm is as follows:

At each step, sort {a, b, c}.
Append the largest valid character (if there're more than one choice, pick any of them) to the answer. "Valid" means appending the character won't form three repeating characters.
Update remaining {a, b, c}.
Repeat step 1-3 until there's no valid character that can be appended.


"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        source = [["a", a], ["b", b], ["c", c]]
        res = []
        
        while True:
            source.sort(key = lambda x: x[1])
            idx = 1 if len(res) >= 2 and res[-1] == res[-2] == source[2][0] else 2
            if source[idx][1]:
                res.append(source[idx][0])
                source[idx][1] -= 1
            else:
                break
        
        return "".join(res)
