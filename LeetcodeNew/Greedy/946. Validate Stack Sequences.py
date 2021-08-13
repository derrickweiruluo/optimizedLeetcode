""""
Solution1: Simulating
Initialize am empty stack,
iterate and push elements from pushed one by one.
Each time, we'll try to pop the elements from as many as possibile popped.
In the end, we we'll check if stack is empty.

## 贪心算法，先模拟push，每当stack顶部 == popped[idx], stack.pop(), idx += 1

Time O(N)
Space O(N)
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack, idx = [], 0
        for push in pushed:
            stack.append(push)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        
        return len(stack) == 0

