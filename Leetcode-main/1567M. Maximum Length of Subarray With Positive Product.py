class Solution: #1567
  #频率2-3
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        pos_len, neg_len = 0, 0
        for num in nums:
            if num > 0:
                pos_len += 1
                neg_len += 1 if neg_len else 0
            elif num < 0:
                temp_pos = pos_len
                pos_len = neg_len + 1 if neg_len else 0
                neg_len = temp_pos + 1
            else:
                pos_len, neg_len = 0, 0
            
            res = max(res, pos_len)
        
        return res
