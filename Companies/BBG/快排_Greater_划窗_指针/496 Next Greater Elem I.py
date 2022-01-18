'''
find the NGE in nums1 corresponding in nums2

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nextGreater = dict()
        stack = []  # Increasing stack of idx
        res = []
        
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:    # pop <= elements on the stack
                stack.pop()
            nextGreater[nums2[i]] = stack[-1] if stack else -1   # 更新dict based on stack, if empty, cur num is the largest (no next greater)
            stack.append(nums2[i])                    # update the stack
            
            
        for i in range(len(nums1)):
            res.append(nextGreater[nums1[i]])
        
        return res



class Solution:   # not the best
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nextGreater = dict()
        stack = []  # Increasing stack
        res = []
        
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                nextGreater[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            
        while stack:
            nextGreater[stack.pop()] = -1
            
        for i in range(len(nums1)):
            res.append(nextGreater[nums1[i]])
        
        return res