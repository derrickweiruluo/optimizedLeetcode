'''
general DP(LIS) solution in Python
https://www.cnblogs.com/grandyang/p/5888439.html
A frog is crossing a river. The river is divided into x units and at each unit there may
or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1 unit.
If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units.
Note that the frog can only jump in the forward direction.
Note:
The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:
[0,1,3,5,6,8,12,17]
There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.
'''

"""
Following is my backtracking solution using dict for memorization.
The memo dict is using for save those dead end. 
So when we get to the same stone with the same speed we don't need to search further.
"""

# DFS + MEMO
import collections
class Solution1:
    def canCross(self, stones):
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        res = self.bt(stones, 1, 1, target)  # i=1 石头开始看， 初始化
        return res

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False
        if cur == target:
            return True
        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False

        # dfs
        candidates = [speed - 1, speed, speed + 1]
        for nextSpeed in candidates:
            if (cur + nextSpeed) in stones:
                if self.backtrack(stones, cur + nextSpeed, nextSpeed, target):
                    return True

        self.memo.add((cur, speed))
        return False


# 1D DP, maintain a longest increasing subsequence
class SolutionDP:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        N = len(stones)
        if N == 0 or (N > 1 and stones[1] != 1):
            return False
			
        dp = [False for _ in range(N)]  # dp[i] means whether stone i can be reached or not
        dp[0] = dp[1] = True
        next_jump = collections.defaultdict(list)   # to record the possible next jumps from stone i
        next_jump[1] = [0, 1, 2]

        for i in range(2, N):
            for j in range(1, i):
                need_jump = stones[i] - stones[j]
                if dp[j] and need_jump in next_jump[j]:
                    dp[i] = True
                    next_jump[i].extend([need_jump, need_jump + 1, need_jump - 1])

        return dp[N - 1]

# DFS + MEMO
class Solution11:
    def canCross(self, stones):
        target, stones, memo = stones[-1], set(stones), set()
        return self.backtrack(stones, 1, 1, target, memo)

    def backtrack(self, stones, pos, jump, target, memo):
        if (pos, jump) in memo:
            return False
        if pos == target:
            return True
        if jump <= 0 or pos not in stones:
            return False
        for j in (jump - 1, jump, jump + 1):
            if self.backtrack(stones, pos + j, j, target, memo):
                return True
        memo.add((pos, jump))  # record bad position and jump
        return False

# BFS + MEMO
class Solution7:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        q = collections.deque()
        v = collections.defaultdict(lambda : collections.defaultdict(bool))
        stoneSet = set(stones)
        q.append((0, 0))
        v[0][0] = True
        while q:
            x, y = q.popleft()
            if x == stones[-1]: return True
            for z in (y - 1, y, y + 1):
                if z > 0 and not v[x + z][z] and x + z in stoneSet:
                    v[x + z][z] = True
                    q.append((x + z, z))
        return False


# 2D DP
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        n = len(stones)
        
        # d[[i][k] = BOOLEAN: jump of size k to reach stones[i]
        
        dp = [[False for _ in range(n + 1)] for _ in range(n)]
        dp[0][1] = True
        
        for i in range(1, n):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff < 0 or diff > n or not dp[j][diff]:
                    continue
                dp[i][diff] = True
                if i == n - 1:
                    return True
                if diff - 1 >= 0:
                    dp[i][diff - 1] = True
                if diff + 1 <= n:
                    dp[i][diff + 1] = True
                
        
        return False