'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.


Input: s = "cccaaa"
Output: "aaaccc"

Input: s = "Aabb"
Output: "bbAa"
'''

# Optimized Bucket Sort  Overall O(n), Space O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        buckets = collections.defaultdict(list)
        
        for char, freq in counter.items():
            buckets[freq].append(char)
        
        res = ""
        
        for freq in range(len(s), -1, -1):  # start from the largest possible freq
            for char in buckets[freq]:
                res += char * freq
        
        
        return res




# Brute forace counter and sorting 
# sort by counter frequency , then the char
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        s = list(s)
        s.sort(key=lambda x:(-cnt[x], x))
        return "".join(s)