class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        pos_nums, neg_nums, zero_nums = [], [], []
        for num in nums:
            if num > 0: pos_nums.append(num)
            elif num < 0: neg_nums.append(num)
            else: zero_nums.append(num)
        
        pos_set, neg_set = set(pos_nums), set(neg_nums)
        
        if zero_nums:
            for num in pos_set:
                if -1 * num in neg_set:
                    res.add((-1 * num, 0, num))
                    
        if len(zero_nums) >= 3: res.add((0, 0, 0))
            
        for i in range(len(pos_nums)):
            for j in range(i + 1, len(pos_nums)):
                complement = -1 * (pos_nums[i] + pos_nums[j])
                if complement in neg_set:
                    res.add(tuple(sorted([pos_nums[i], pos_nums[j], complement])))
        
        for i in range(len(neg_nums)):
            for j in range(i + 1, len(neg_nums)):
                complement = -1 * (neg_nums[i] + neg_nums[j])
                if complement in pos_set:
                    res.add(tuple(sorted([neg_nums[i], neg_nums[j], complement])))
                    
        return res
