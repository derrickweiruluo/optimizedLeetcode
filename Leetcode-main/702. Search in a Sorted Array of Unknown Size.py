# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        
        left, right = 0, 1
        # 定boundary
        while reader.get(right) < target:
            left = right
            right <<= 1
            print(left, right)
        # 基操
        while left < right:
            mid = left + (right - left) // 2
            if reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid
            
        return -1 if reader.get(left) != target else left
                
        
