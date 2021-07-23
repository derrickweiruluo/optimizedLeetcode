class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        
        def canFitMore(val):
            res, cur = 1, position[0]
            for i in range(1, n):
                if position[i] - cur >= val:
                    res += 1
                    if res >= m:
                        return True
                    cur = position[i]
            return False
        
        left, right = 1, position[-1] - position[0] + 1
        while left < right:
            # mid = right - (right - left) // 2
            mid = left + (right - left) // 2
            if canFitMore(mid):
                left = mid + 1
            else:
                right = mid
                
        return right - 1
