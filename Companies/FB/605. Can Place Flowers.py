'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.


Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

'''

class Solution: # BEST
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        length = len(flowerbed)
        res = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                res += 1
                flowerbed[i] = 1
            if res >= n:
                return True
        
        return False



class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        res = 0
        
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                print(i)
                flowerbed[i] = 1
                res += 1
        print(res)
        return res >= n