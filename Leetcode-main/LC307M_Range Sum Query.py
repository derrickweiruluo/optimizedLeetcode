class NumArray:
# 不可以用每个index的累积sum来求解（308, TLE
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.seg_tree = [0 for i in range(len(nums)*2)]
        for i in range(len(nums)):
            j = i + len(nums)
            self.seg_tree[j] = nums[i]
        for i in range(len(nums)-1 , 0, -1):
            self.seg_tree[i] = self.seg_tree[i*2] + self.seg_tree[i*2+1]

    def update(self, index: int, val: int) -> None:
        j = index + len(self.nums)
        diff = val - self.seg_tree[j]
        while(j > 0):
            self.seg_tree[j] += diff
            j = j//2
            
        

    def sumRange(self, left: int, right: int) -> int:
        i = left + len(self.nums)
        j = right + len(self.nums)
        sum = 0
        while (i <= j):
            if(i % 2 == 1):
                sum += self.seg_tree[i]
                i+=1
            if(j % 2 == 0):
                sum += self.seg_tree[j]
                j-=1
            i = i//2
            j = j//2
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
