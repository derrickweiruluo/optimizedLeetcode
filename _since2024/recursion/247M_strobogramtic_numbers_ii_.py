"""
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]
 

Constraints:

1 <= n <= 14
"""


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = [""] if n % 2 == 0 else ["0", "1", "8"]

        for _ in range(n // 2):  # froming the answer rom the middle of the length 
            cur = []
            for num in res:
                cur.append("1" + num + "1")
                cur.append("8" + num + "8")
                cur.append("6" + num + "9")
                cur.append("9" + num + "6")
                if len(num) < n - 2: # this is to prevent trailing and ending zeros
                    cur.append("0" + num + "0")
            res = cur

        return res
