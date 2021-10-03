'''91 Decode Ways

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1 # 因为有单双digit解密方法
        
        
        # dp[0] = 1 as long as the first digit is not 0
        # scanning:  '226': [22]6 --> 2[26]
        # 只有从第二个digit才会扫两种可能性

        for i in range(2, len(s) + 1):
            if int(s[i - 1: i]) > 0:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        
        
        
        print(dp)
        return dp[-1]