'''
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

1.  Add a positive integer to an element of a given index in the array nums2.
2.  Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value 
'''

# Clarification  nums2 >> nums1


class FindSumPairs:

# Time:
# Constructor: O(nums2.length)
# Add: O(1)
# Count: O(nums1.length)
    
# Space: O(nums2.length)
    
    def __init__(self, nums1: List[int], nums2: List[int]):
        # Initializes the FindSumPairs object with two integer arrays nums1 and nums2.

        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = collections.Counter(nums2)
    
    def add(self, index: int, val: int) -> None:
        # void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
        self.freq2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        # int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
        res = 0
        for num in self.nums1:
            res += self.freq2[tot - num]
        
        return res