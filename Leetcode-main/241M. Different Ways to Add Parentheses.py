class Solution:   # 241. Different Ways to Add Parentheses
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit(): return [int(expression)]
        res = []
        
        def compute(left, right, op):  
            if op == '-': return left - right
            elif op == '+': return left + right
            else: return left * right
        
        
        for i, val in enumerate(expression):
            if val in "+-*":
                left = self.diffWaysToCompute(expression[:i])  # 递归左半段
                right = self.diffWaysToCompute(expression[i+1:])   # 递归右半段
                res.extend([compute(l, r, val) for l in left for r in right]) #两边的range 交叉运算，取决于当前切割点的op
                
        return res
