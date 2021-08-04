"""
需要trick， identify 5 个候选人最重要
base case， 解在[9999, 100001] for any 5-digit number
prefix 是 input_str[:mid], where mid = (len + 1) // 2

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. 
If there is a tie, return the smaller one.
The closest is defined as the absolute difference minimized between two integers.

Example 1:
Input: n = "123"
Output: "121"

Example 2:
Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

"""

class Solution:
    def nearestPalindromic(self, n: str) -> str:
      
        digits = len(n)
        
        # intial TWO candidates(bounds):    9999 <<  any 5-digit num  << 100001
        # prefix for odd/even len(n), ex: prefix = 3 for n == 5 and 6
        candidates = set((str(10 ** digits + 1), str(10 ** (digits - 1) - 1)))
        prefix = int(n[:(digits + 1) // 2])
        
        # add addtional 3 more candidates based  on the prefix [-1, 0, 1] from prefix
        # add the increment based on odd/even
        for start in (str(prefix - 1), str(prefix), str(prefix + 1)):
            if digits % 2 == 0:
                cand = start + start[::-1]
                candidates.add(cand)
            else:
                cand = start + start[:-1][::-1]
                candidates.add(cand)
            
        candidates.discard(n)    # the delele input num 
        print(candidates)
        # return smallest, sort by abs(diff), then by value
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

"""
1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
"""
