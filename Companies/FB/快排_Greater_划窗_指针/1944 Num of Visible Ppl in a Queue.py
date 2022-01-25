# similar next greater
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/1359868/JavaPython-3-Monotonic-increasing-stack-w-18-similar-problems-brief-explanation-and-analysis.

# https://leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/1359707/JavaC%2B%2BPython-Stack-Solution-Next-Greater-Element


# We maintain a decreasing mono stack,
# (I stored the index of elements)

# As we iterate each element a in input array A,
# assume the last element in the stack has index i.
# If the last element A[i] <= a,
# A[i] can see a,
# so we increment res[i]++


# ClarificationsL:
# A person can see another person to their right in the queue if everybody in between is SHORTER than both of them.
# All the values of heights are unique.
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        res = [0] * n
        stack = []

        # for loop update for each i, 
        # res[i] += decreasing Cnt + optional taller ppl as the right bound

        for i in range(n - 1, -1, -1):
            while stack and heights[i] >= heights[stack[-1]]:
                res[i] += 1
                
                # each pop(), cur ppl seen += 1, and will be invisible for
                # the next ppl on the left, which also maintain mono
                stack.pop()
            
            # 如果pop完，还剩下一个比自己高的在far right, res += 1
            if stack:
                res[i] += 1
            # print(i, stack)
            stack.append(i)
        
        return res


# Test Cases:

# heights = [5,1,2,3,10]
# res     = [0,0,0,0,0]
# # ---------------------------
# res     = [0,0,0,0,0]   stack = [10]
# res     = [0,0,0,1,0]   stack = [3,10],     res[i] += 0 + 1
# res     = [0,0,1,1,0]   stack = [2,3,10]    res[i] += 0 + 1
# res     = [0,1,1,1,0]   stack = [1,2,3,10]  res[i] += 0 + 1
# res     = [4,1,1,1,0]   stack = [10]        res[i] += 1 + 3

# res: [4,1,1,1,0]


# *-----------------------------

class Solution: # just clean code
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # https://leetcode.com/submissions/detail/599939887/
        # https://leetcode.com/submissions/detail/599939496/
        
        stack = []
        n = len(heights)
        res = [0] * n
        
        
        for i in range(n - 1, -1, -1):
            while stack and heights[i] >= heights[stack[-1]]:
                res[i] += 1
                stack.pop()
            if stack:
                res[i] += 1
            stack.append(i)
        
        return res