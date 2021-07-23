class Solution:
#   easy 高频，stack基操 amazon ms
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        stack = []
        res = []
        
        for num in nums2:  #利用stack的顺序来找到nums2每个位置的next higher，while loop一直pop
            while stack and stack[-1] < num:
                dict[stack.pop()] = num
            stack.append(num)
        
        while stack:  #其他stack上落单的 = -1
            dict[stack.pop()] = -1
        
        for num in nums1:
            res.append(dict[num])
            
        return res
