'''
Look for duplicates:

1.  nums[i] == nums[j]
2.  abs(i - j) <= k

'''


class Solution:  # GOOD
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i, val in enumerate(nums):
            if val in mapping and i - mapping[val] <= k:
                return True
            mapping[val] = i
            
        return False
        
        
        
class Solution:  # not concise
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = collections.defaultdict(list)
        for i, num in enumerate(nums):
            mapping[num].append(i)
        
        for num in sorted(mapping):
            lst = mapping[num]
            for i in range(len(lst) - 1):
                if lst[i + 1] - lst[i] <= k:
                    return True
        
        return False
                