'''
An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.




Input: n = 5
Output: [3,1,2,5,4]

inout: n = 6
Output: [1,5,3,2,6,4]
'''

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        # 换句话老说，要求 left, mid, right
        # mid 一定是偶数
        # left, right = odd + even
        
        
        res = [1]
        while len(res) < n:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
            print(res)
        
        return [i for i in res if i <= n]
    
#         n = 6
#         res     [1]
#         res     [1, 2]
#         res     [1,3] + [2,4] -> [1,3,2,4]
#         res     [1,5,3,7] + [2,6,4,8]  -> [1,5,3,7,2,6,4,8]
        
#         trim to [1,5,3,7,2,6]

# Recursive
class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        return self.helper(range(1,N+1))
        
    def helper(self, lst):
        if len(lst)<=2:         return lst
        return self.helper(list(lst[::2])) + self.helper(list(lst[1::2]))