'''
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
'''

class Solution: # Two pointers, just you array 
    def firstUniqChar(self, s: str) -> int:
        
        if not s: return -1
        n = len(s)
        if n == 1: return 0
        s = list(map(str, s))    
        
        counter = [0] * 256
        counter[ord(s[0]) - ord('a')] = 1
        
        i = 0 # slow pointer
        
        # for j, char in enumerate(s, start = 1):
        for j in range(1, n):
            counter[ord(s[j]) - ord('a')] += 1
            while i < n and counter[ord(s[i]) - ord('a')] > 1:
                i += 1
        
        return i if i < n else -1


class Solution:  # hashmap 
    def firstUniqChar(self, s: str) -> int:
        mapping = {}
        for i, val in enumerate(s):
            mapping[val] = mapping.get(val, []) + [i]
        
        for char, lst in mapping.items():
            if len(lst) == 1:
                return mapping[char][0]
        
        return -1


class Solution: # two pointers and hashmap
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        n = len(s)
        if n == 1: return 0
        slow, fast = 0, 1
        count = collections.defaultdict(int)
        
        arr = list(map(str, s))
        # print(arr)
        count[arr[slow]] += 1

        while fast < n:
            count[arr[fast]] += 1
            while slow < n and count[arr[slow]] > 1:
                slow += 1
            if slow >= n:
                return -1
            fast += 1
        
        return slow



