"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392939/PythonC%2B%2BJava-Stack-Based-Solution-Clean-and-Concise


This is one of that problems where you need to understand what is the topic: if you do it, then you will solve it, if you not, you can strugle quite a lot. Notice that here we consider groups of elements with the same value which are adjacent. If we delete them, another symbols will become adjacent. Stack is just ideal for this purposes.

So, we keep stack with pairs of elements: element itself and its frequency. Also I put in the beginning dummy variable, so I do not need to check if stack is empty. For each element we:

Check if it is equal to the last element in stack, if it is, increase it frequency, if not - create new instance in stack with frequency 1.
Check if we can delete groups of k equal elements: check if last frequency in stack is >=k and if it is, decrease it. Also if we get frequency equal to 0, delete element at all.
Complexity
It is just O(n) for time and space: we proceed every element at most twice: to put it to stack and to remove it from stack.

"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []                  # stack of [char, freq]
        
        for i, char in enumerate(s):
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            # check stack[-1][1]'s frequency before go to next index
            if stack[-1][1] == k:   # only buidling the char from freq 0 to k - 1
                stack.pop()         # so the stack[-1][1]'s frequency will never >= k
        
        return "".join(char * freq for char, freq in stack)
