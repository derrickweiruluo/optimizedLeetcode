'''
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]


(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''

# 给一个运算加括号，问有最多几种解(allows duplicates)

class Solution:
    def diffWaysToCompute(self, input):
        memo = {}
        return self.dfs(input, memo)
        
    def dfs(self, expression, memo):
        if expression in memo:
            return memo[expression]
        if expression.isdigit():
            memo[expression] = int(expression)
            return [int(expression)]
        res = []
        for i, c in enumerate(expression):
            if c in "+-*":
                l = self.diffWaysToCompute(expression[:i])
                r = self.diffWaysToCompute(expression[i+1:])
                res.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        memo[expression] = res
        return res



class Solution:   # 241. Different Ways to Add Parentheses
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit(): return [int(expression)]
        
        self.memo = collections.defaultdict(list)
        res = []
        
        def compute(left, right, op):
            cur = str(left) + '#' + str(right) + '#' + op
            if cur in self.memo:
                return self.memo[cur]
            if op == '-': 
                self.memo[cur] = left - right
                return left - right
            elif op == '+': 
                self.memo[cur] = left + right
                return left + right
            else: 
                self.memo[cur] = left * right
                return left * right
            
        
        
        for i, val in enumerate(expression):
            if val in "+-*":
                left = self.diffWaysToCompute(expression[:i])  # 递归左半段
                right = self.diffWaysToCompute(expression[i+1:])   # 递归右半段
                
                #两边的range 交叉运算，取决于当前切割点的op
                res.extend([compute(l, r, val) for l in left for r in right]) 
                
        return res


