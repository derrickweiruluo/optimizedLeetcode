import collections
import heapq



# https://leetcode.com/problems/top-k-frequent-words/discuss/933479/Python3-Trie-%2B-bucket-sort
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.word = None

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = collections.Counter(words)
        buckets = [TrieNode() for _ in range(len(words) + 1)]
        for w in counter:
            root = buckets[counter[w]]
            self.add(w, root)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i].children:
                continue
            self.getWord(res, buckets[i], k)
            if len(res) >= k:
                return res
        
        return res
    
    def add(self, word, root):
        for c in word:
            if root.children[ord(c) - ord("a")] == None:
                root.children[ord(c) - ord("a")] = TrieNode()
            root = root.children[ord(c) - ord("a")]
        root.word = word
    
    def getWord(self, res, root, k):
        if not root: return
        if len(res) >= k: return
        if root.word:
            res.append(root.word)
        for i in range(26):
            self.getWord(res, root.children[i], k)
        return


#* -------------------

class Solution:
    # Time Complexity = O(n + nlogk)
    # Space Complexity = O(n)
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word