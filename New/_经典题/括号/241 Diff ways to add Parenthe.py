'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 
Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10





Time Complexity: O(N * 2^N)
Let N be the length of the expression
In the worst case there are N // 2 operations: when all expression numbers are numbers of 1 digits
For example, expression: 1+2+3+4+5+6
len(expression) = 11
operations # = 5
Therefore, our recursion depth is O(N/2)
		depth         Nbr of problem           work at corresponding depth
		0             1                        O(N) #divide expression
		1             2                        O(1) + O(N - 2) = O(N) * 2
		...
		i             2^i                      O(N) * 2^i 
		...
		N//2          2^N//2                   O(N) * 2^N//2

		Total time complexity: O(N) (2^0 + 2^1 + ... + 2^N//2) = O(N * 2^N//2) = O(N * 2^N)
        
'''

class Solution:   # Same as below, add memo for speed up
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
                
                #两边的range 交叉运算，取决于当前切割点的op
                res.extend([compute(l, r, val) for l in left for r in right]) 
                
        return res

# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.