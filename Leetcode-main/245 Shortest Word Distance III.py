class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        
        arr1, arr2 = [], []
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                arr1.append(i)
            elif wordsDict[i] == word2:
                arr2.append(i)
        
        i = j = 0
        
        res = len(wordsDict)
        if word1 == word2:
            return min(arr1[i] - arr1[i - 1] for i in range(1, len(arr1)))
        
        while i < len(arr1) and j < len(arr2):
            res = min(res, abs(arr1[i] - arr2[j]))
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        
        return res
            



#         # METHOD 2
#         n = len(wordsDict)
#         res = n
        
#         pointer1 = pointer2 = -1  # start at the last BUT only check if they are >= 0
        
#         for i, word in enumerate(wordsDict):
#             if word == word1:
#                 pointer1 = i
#                 if pointer2 >= 0 and pointer1 != pointer2:
#                     res = min(res, abs(pointer1 - pointer2))
                    
#             if word == word2:
#                 pointer2 = i
#                 if pointer1 >= 0 and pointer1 != pointer2:
#                     res = min(res, abs(pointer1 - pointer2))
                    
#         return res
