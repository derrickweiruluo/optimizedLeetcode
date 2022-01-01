
'''
A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

1.  age[y] <= 0.5 * age[x] + 7
2.  age[y] > age[x]
3.  age[y] > 100 && age[x] < 100
4.  1 <= ages[i] <= 120
'''

# 满足以上任意条件的就会 发出 friend request， 问一共有多少条 request



# Time Complexity: O(N) + O((120 - 15) ^ 2) ~ O(N)
# Space Complexity: O(121) ~ O(1)
class Solution:  # Interview
    def numFriendRequests(self, ages: List[int]) -> int:
        
        def validReq(x, y):
            if y <= 0.5 * x + 7 or y > x or (y > 100 and x < 100):
                return False
            return True
        
        res = 0
        counter = collections.Counter(ages)
        
        # condition 2: age[B] > 100 && age[A] < 100
        for age1 in range(15, 121):
            # condition 0: age[B] <= 0.5 * age[A] + 7
            # condition 1: age[B] > age[A]
            for age2 in range(age1 // 2 + 8, age1 + 1):
                if age1 != age2:
                    res += counter[age2] * (counter[age1])
                else:
                    res += counter[age2] * ((counter[age1]) - 1)
        
        # print(counter)
        return res



class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        def validReq(x, y):
            if y <= 0.5 * x + 7 or y > x or (y > 100 and x < 100):
                return False
            return True
        res = 0
        counter = collections.Counter(ages)
        for x, freqX in counter.items():
            for y, freqY in counter.items():
                if validReq(x, y):
                    res += freqX * freqY
                    if x == y: 
                        res -= freqX

        return res



# A O(NlogN) approach using binary search:

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = 0
        N = len(ages)
        ages.sort()
        for i in range(N):
            a = ages[i]
            idx1 = bisect.bisect(ages, a)
            idx2 = bisect.bisect(ages, 0.5 * a + 7)
            cnt += max(0, idx1 - idx2 - 1) 
        return cnt