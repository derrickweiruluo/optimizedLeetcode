class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        counter = {}
        for num in target:
            if num in counter.keys():
                counter[num] += 1
            else:
                counter[num] = 1
        
        for num in arr:
            if num not in counter or counter[num] == 0:
                return False
            counter[num] -= 1
        
        for k, v in counter.items():
            if v != 0:
                return False
        
        return True
        
        