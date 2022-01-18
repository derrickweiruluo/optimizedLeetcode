'''
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

# if there is common prefix, it must within the shortest string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        # maxStr = max(strs)
        # minStr = min(strs)
        strs.sort(key = lambda x: (x, len(x)))
        maxStr = strs[-1]
        minStr = strs[0]

        for idx, char in enumerate(minStr):
            if char != maxStr[idx]:
                return minStr[:idx]
        
        return minStr



