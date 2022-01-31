'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
'''



# Follow up: What if only one of the vectors is sparse?
# time: O(len(shorter dictionary))
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

# Advance      
# above are hashmap solutions, META wants non-hashmap

class SparseVector:
    def __init__(self, nums: List[int]):
        indexes = []
        vals = []
        for i, num in enumerate(nums):
            if num != 0:
                indexes.append(i)
                vals.append(num)
        self.indexes = indexes
        self.vals = vals

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        m, n = len(self.indexes), len(vec.indexes)
        i = j = 0
        while i < m and j < n:
            if self.indexes[i] == vec.indexes[j]:
                res += self.vals[i] * vec.vals[j]
                i += 1
                j += 1
            elif self.indexes[i] < vec.indexes[j]:
                # Advance i using binary search (instead of i += 1)
                i = bisect.bisect_left(self.indexes, vec.indexes[j], lo = i + 1)
            else:
                # Advance j using binary search (instead of j += 1)
                j = bisect.bisect_left(vec.indexes, self.indexes[i], lo = j + 1)
        
        return res