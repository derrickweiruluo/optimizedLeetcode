'''
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        
        res = '1'    # base case
        
        def convert(s):
            res = ''
            s += '#'   # just for making the the comparison easier at the last index
            print(s)
            cnt = 1
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    cnt += 1
                else:
                    res += str(cnt) + s[i]
                    cnt = 1
            return res
        
        for _ in range(n - 1):
            res = convert(res)
        
        return res