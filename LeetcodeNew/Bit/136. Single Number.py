class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
#         位运算， 相同bit XOR 结果为 0
#         所以只要start from 0， XOR the whole array
        
#         ***  XOR ****
        
        res = 0
        for num in nums:
            res ^= num
        
        return res
        
