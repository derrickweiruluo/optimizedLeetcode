'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
'''



# Follow up: What if only one of the vectors is sparse?
# time: O(N)
# space O(L), only non-zero takes spaces

class SparseVector:  #最优解
    def __init__(self, nums: List[int]):
        self.memo = {}
        self.length = len(nums)
        for i, val in enumerate(nums):
            if val != 0:
                self.memo[i] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        d1, d2 = {}, {}  # only iterate the shorter vector by comparing length
        
        if self.length > vec.length:
            d1, d2 = vec.memo, self.memo
        else:
            d1, d2 = self.memo, vec.memo
        
        res = 0
        for idx in d1:
            if d1[idx] and idx in d2:
                res += d1[idx] * d2[idx]
        
        return res

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)