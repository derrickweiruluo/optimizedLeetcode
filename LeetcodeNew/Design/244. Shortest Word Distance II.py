'''
Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.


EX1 :
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]
'''

class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.maxLen = len(wordsDict)
        self.memo = collections.defaultdict(list)
        for idx, w in enumerate(wordsDict):
            self.memo[w].append(idx)
        
    def shortest(self, word1: str, word2: str) -> int:
        arr1, arr2 = self.memo[word1], self.memo[word2]
        res = self.maxLen
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            res = min(res, abs(arr1[i] - arr2[j]))
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        return res