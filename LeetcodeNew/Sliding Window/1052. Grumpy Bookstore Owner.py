class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        originalGain = 0
        maxGain = curSave = 0
        
        for i in range(n):
            # 叠加原来的gain when 老板开心
            if grumpy[i] == 0:
                originalGain += customers[i] 
            
            # sliding window of potential saving 
            curSave += grumpy[i] * customers[i] 
            if i > X - 1:
                curSave -= customers[i-X] * grumpy[i-X] # 
            maxGain = max(maxGain, curSave)
        
        return originalGain + maxGain