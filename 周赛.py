# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# 656101987
# 1

def minMoves(target: int, maxDoubles: int) -> int:
    res = 0
    while target > 1:
        if target % 2 == 1:
            target -= 1
            res += 1
        elif maxDoubles and target % 2 == 0:
            target = target //2
            maxDoubles -= 1
            res += 1
        else:
            target -=1
            res += 1
    return res 
a = minMoves(656101987, 1)
print(a)



def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        
        n = len(nums)
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        print(pos)
        print(neg)
        idx1, idx2 = 0, 0
        
        res = [0] * n
        for i in range(n):
            if i % 2 == 0:
                res[i] = pos[idx1]
                idx1 += 1
            else:
                res[i] = neg[idx2]
                idx2 += 1
        
        return nums