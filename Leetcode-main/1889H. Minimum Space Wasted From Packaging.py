class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        preSum = [0]
        curr = 0
        for p in packages:
            curr += p
            preSum.append(curr)
        
        res = math.inf
        for supply in boxes:
            supply.sort()
            if supply[-1] < packages[-1]:
                continue
                
            currWaste = 0
            prev = 0
            
            for box in supply:
                idx = bisect.bisect_right(packages, box)
                currWaste += box * (idx - prev) - (preSum[idx] - preSum[prev])
                prev = idx
            
            res = min(res, currWaste)
        
        return -1 if res == math.inf else res % (10**9 + 7)
    
