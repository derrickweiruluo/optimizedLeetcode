

# DFS + MEMO
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.memo = set()  # failureSet
        target = stones[-1]
        stones = set(stones)
        res = self.backtrack(stones, 1, 1, target)
        return res
    
    def backtrack(self, stones, cur, speed, target):
        if (cur, speed) in self.memo:
            return False
        if cur == target:
            return True
        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False
        candidates = [speed - 1, speed, speed + 1]
        for c in candidates:
            if (cur + c) in stones:
                if self.backtrack(stones, cur + c, c, target):
                    return True
        
        self.memo.add((cur, speed))
        return False


"""
The problem is a member of the longest increasing subsequence problems family which is called LIS usually. 
And its DP solution is also general. It looks very consice.
"""
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