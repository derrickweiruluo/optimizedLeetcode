class Solution:
  #频率 1， 没公司，xor特性更值得
    def countTriplets(self, arr: List[int]) -> int:
        
        # Method 1, O(n) 这题的trick只apply到这一题，没代表性，xor特性更重要
        res, cur = 0, 0
        count = {0 : 1}
        sum = {0 : 0}
        for i, val in enumerate(arr):
            cur ^= val #累计 xor值
            freq = count.get(cur, 0) #get freq hashmap,   default 0
            preSum = sum.get(cur, 0) #get preSum hashmap,  default 0
            count[cur] = freq + 1
            sum[cur] = preSum + i + 1
            
            res += i * freq - preSum
            # print(n, total)
        
        return res
    
# Method 2, O(n^2), 面试想出来更有可能，这题的trick只apply到这一题，没代表性，xor特性更重要
        # res = 0
        # arr.insert(0, 0)
        # n = len(arr)
        # for i in range(n - 1):
        #     arr[i + 1] ^= arr[i]
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if arr[i] == arr[j]:
        #             res += j - i - 1
        # return res
