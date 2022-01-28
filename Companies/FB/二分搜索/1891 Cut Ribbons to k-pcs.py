'''
Example 1:

Input: ribbons = [9,7,5], k = 3
Output: 5
'''


# Clairifcations:
# you can throw exessive robin
# return the max result
# k could be bigger than any exisiting ribon length

import collections
class Solution: # BS-template 1 -- Interview
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        total, maxRib = sum(ribbons), min(ribbons)
        if k > total: return 0
        
        left, right = 1, max(total // k + 1, maxRib) + 1     # upperbound for speed
        counter = collections.Counter(ribbons)          # speed improvement
        
        def canCut(length, k):
            res = 0
            for ribbon in counter:
                res += (ribbon // length) * counter[ribbon]
                if res >= k:
                    return True
            return False
        
        # find the lower bound of the first invalid answers
        # therefore, the converged result is the first invalid
        # thus return left - 1
        while left < right:
            mid = (left + right) // 2
            if canCut(mid, k):
                left = mid + 1
            else:
                right = mid
        
        return left - 1





class Solution: # BS-template 2
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        total, maxRib = sum(ribbons), max(ribbons)
        left, right = 1, max(total //k, maxRib)
        
        if k > total: return 0
        
        def canCut(length, k):
            res = 0
            for ribbon in ribbons:
                res += ribbon // length
                if res >= k:
                    return True
            return False
        
        # find the lower bound of the first invalid answers
        # therefore, the converged result is the first invalid
        # thus return left - 1
        while left <= right:
            mid = (left + right) // 2
            if canCut(mid, k):
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1