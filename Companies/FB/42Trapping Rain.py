'''
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        if n < 3:
            return 0
        
        left_bound, right_bound = height[0], height[-1]
        volume = 0
        
        left, right = 0, n - 1
        while left < right:
            left_bound = max(left_bound, height[left])
            right_bound = max(right_bound, height[right])
            
            if left_bound < right_bound:
                volume += left_bound  - height[left]
                left += 1
            else:
                volume += right_bound - height[right]
                right -= 1
        
        return volume