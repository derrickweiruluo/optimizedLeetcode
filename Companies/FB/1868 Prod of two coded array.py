'''
The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:

Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
Compress prodNums into a run-length encoded array and return it.
'''

'''EX 1'''
# encoded1 = [[1,3],[2,3]]
# encoded2 = [[6,3],[3,3]]

# encoded1 expands to [1,1,1,2,2,2]
# encoded2 expands to [6,6,6,3,3,3].

# prodNums = [6,6,6,6,6,6]
# Final: [6:6]

'''EX 2'''
# encoded1 = [[1,3],[2,1],[3,2]]
# encoded2 = [[2,3],[3,3]]

# encoded1 expands to [1,1,1,2,3,3] 
# encoded2 expands to [2,2,2,3,3,3]
# prodNums = [2,2,2,6,9,9], which is compressed into 

# [[2,3],[6,1],[9,2]].



class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        
        i = j = 0
        
        while i < len(encoded1) and j < len(encoded2):
            val_1, freq_1 = encoded1[i]
            val_2, freq_2 = encoded2[j]
            product = val_1 * val_2
            prodFreq = min(freq_1, freq_2)
            
            encoded1[i][1] -= prodFreq
            encoded2[j][1] -= prodFreq
            
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
            
            if not res or res[-1][0] != product:
                res.append([product, prodFreq])
            else:
                res[-1][1] += prodFreq
        
        return res