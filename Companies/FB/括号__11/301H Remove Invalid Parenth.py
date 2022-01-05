'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

'''
# https://github.com/wisdompeak/LeetCode/tree/master/DFS/301.Remove-Invalid-Parentheses
# 本题没有太高明的办法，基本就是靠搜索，数量级应该就是O(2^N).DFS和BFS均可。感觉对于在同一个数组或字符串里面搜若干个元素的话，DFS写起来更舒服一些。基本思想就是对于每一个s[i]都有“选用”（append到当前curStr中去）和“不选用”两种选择，然后依次递归下去。如果遇到curStr不合法的情况，就及时中断这条支路。

class Solution:  # BEST
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        if not s: return [""]
        level = set([s])            # initial BFS as set
        
        # construct BFS levels (subtring that missing one char), each level could be the final res
            # by doing this, res.append(valid_elem), return the res once it is not null
            # this satisfy the question:
                  # 1, minimum removal
                  # 2, all possible results, at the same BFS level
                    
        queue = collections.deque([s])
        res = []
        visited = set([s])
        
        while queue:
            curLevel = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                curLevel.append(cur)
                if self.isValid(cur):
                    res.append(cur)
            if res:
                # print(curLevel)
                return res
            
            else:
                for elem in curLevel:
                    for i in range(len(elem)):
                        if elem[i] in "()":
                            subStr = elem[:i] + elem[i + 1:]
                            if subStr not in visited:
                                queue.append(subStr)
                                visited.add(subStr)

    def isValid(self, s):
        balance = 0
        for ch in s:
            if balance < 0:
                return False
            if ch == "(":
                balance += 1
            elif ch == ")":
                balance -= 1
        
        return balance == 0


#* --------------------

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        level = set([s])            # initial BFS as set
        
        while True:
            level_res = []          # smallest res is ""
            for elem in level:
                if self.isValid(elem):
                    level_res.append(elem)
            
            # construct BFS levels (subtring that missing one char), each level could be the final res
            # by doing this, res.append(valid_elem), return the res once it is not null
            # this satisfy the question:
                  # 1, minimum removal
                  # 2, all possible results, at the same BFS level
            if level_res:
                return level_res
            
            next_level = set()
            for elem in level:
                for i in range(len(elem)):
                    next_level.add(elem[:i] + elem[i + 1:])
            
            level = next_level
            
    
    def isValid(self, s):
        balance = 0
        for ch in s:
            if balance < 0:
                return False
            if ch == "(":
                balance += 1
            elif ch == ")":
                balance -= 1
        
        return balance == 0