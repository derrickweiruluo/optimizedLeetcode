'''
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.
'''


# input: [1,1,2,2,2,2,4,4]
# output:[1,1,2,2]

# input: [4,2,0]
# output:[]


class Solution1A:  # time O(n + klogk), space O(k)
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) % 2: return []      # check 1，奇数个数的nums直接返回失败
        
        counter = collections.Counter(changed)
        if counter[0] % 2: return []        # check 2, 奇数个数的0直接返回失败
        
        # algorithm
        for key in sorted(counter):
            if counter[key] > counter[key * 2]:
                return []
            if key == 0:
                counter[key] //= 2
            else:
                # 这一步会吧对应的 doubled 消掉，不会被for loop到
                counter[key * 2] -= counter[key]
        
        
        res = []
        for num in counter:
            res += [num] * counter[num]
        
        return res
        # print(counter)
        # return list(counter.elements())



class Solution1B:   # time O(n), space O(k)
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) % 2: return []      # check 1，奇数个数的nums直接返回失败
        
        minVal, maxVal = math.inf, -math.inf
        counter = collections.defaultdict(int)
        for num in changed:
            minVal, maxVal = min(minVal, num), max(maxVal, num)
            counter[num] += 1
        if counter[0] % 2: return []        # check 2, 奇数个数的0直接返回失败
        
        # algorithm
        for num in range(minVal, maxVal + 1):
            if num in counter:
                if counter[num] > counter[num * 2]:
                    return []
                if num == 0:
                    counter[num] //= 2
                else:
                    # 这一步会吧对应的 doubled 消掉，不会被for loop到
                    counter[num * 2] -= counter[num]
        
        
        res = []
        for num in counter:
            res += [num] * counter[num]
        
        return res



# https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470959/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
    # Python, O(N + KlogK)
    # LEE 215
        c = collections.Counter(changed)
        if c[0] % 2:
            return []
        for x in sorted(c):
            if c[x] > c[2 * x]:
                return []
            c[2 * x] -= c[x] if x else c[x] / 2
        return list(c.elements())