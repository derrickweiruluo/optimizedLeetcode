class Solution: #1231
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        
        left, right = 0, 10**9
        
        def canEat(mid):
            count, cur = 0, 0
            for i in range(len(sweetness)):
                cur += sweetness[i]
                if cur >= mid:
                    cur = 0
                    count += 1
            return count > K
        
        while left < right:
            mid = left + (right - left + 1) // 2
            if canEat(mid):
                left = mid
            else:
                right = mid - 1
                
        return left
