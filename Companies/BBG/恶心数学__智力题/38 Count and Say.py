'''
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''

# https://leetcode.com/problems/count-and-say/discuss/16382/Python-easy-to-understand-iterative-and-recursive-solutions

# iterative
class Solution:
    def countAndSay(self, n: int) -> str:
        
        res = '1'    # base case
        
        def convert(s):  # updated fcn
            cnt = 1
            res = ''
            idx = 0
            while idx < len(s):
                cnt = 1
                while idx + 1 < len(s) and s[idx + 1] == s[idx]:
                    cnt += 1
                    idx += 1
                res += str(cnt) + s[idx]
                idx += 1
            return res
        
        # count and say n -1 times, since say(1) is already initialized as 1
        for _ in range(n - 1):
            res = convert(res)
        
        return res


# recursive
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        i, res = 0, ""
        while i < len(s):
            count = 1
            while i+1 < len(s) and s[i+1] == s[i]:
                count += 1
                i += 1
            res += str(count) + s[i]
            i += 1
        return res