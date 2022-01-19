'''
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        leftBound, rightBound = height[0], height[-1]
        
        left, right = 0, len(height) - 1
        res = 0 # volume
        
        while left < right:
            leftBound = max(leftBound, height[left])
            rightBound = max(rightBound, height[right])
            if leftBound < rightBound:
                res += leftBound - height[left]
                left += 1
            else:
                res += rightBound - height[right]
                right -= 1
        
        return res