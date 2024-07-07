"""
Input: arr = [40,10,20,30]
Output: [4,1,2,3]

Input: arr = [100,100,100]
Output: [1,1,1]

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranking = {}

        for num in sorted(arr):
            # if num not found in the ranking, set default to len + 1
            ranking.setdefault(num, len(ranking) + 1)
        
        return map(ranking.get, arr)  # map each element in the array to its corresponding v in a dictionary
