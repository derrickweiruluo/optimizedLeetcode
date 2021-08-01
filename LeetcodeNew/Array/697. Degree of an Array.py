class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        freq_map = collections.defaultdict(list)
        
        for idx, num in enumerate(nums):  
            freq_map[num].append(idx)                  # { num:[ idx_list ] }
        
        
        degree = len(max(freq_map.values(), key=len))  # find the degree by the max_len in the defaultdict(list)
        # print(degree)
        
        
        res = math.inf
        for lst in freq_map.values():
            # print(type(lst), lst)
            if len(lst) == degree:
                res = min(res, lst[-1] - lst[0] + 1)
        
        
        return res
