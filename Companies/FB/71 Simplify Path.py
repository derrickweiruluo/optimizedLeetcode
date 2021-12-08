class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for element in path.split("/"):
            if stack and element == "..":
                stack.pop()
            elif element not in ["", ".", ".."]:
                stack.append(element)
        
        return "/" + "/".join(stack)
    
    
# When you see this problem, you should think about stack. Why? Because we have directories and you can go deeper or come back and when you come back, you basically forgot about all element after and stack is ideal simulation of this process. Also in python you can use .split("/") function, which will split our string into parts, separated by / symbol.

# So, the algorithm will look like this:

# If stack is not empty and we meet .. element, it means, that we need to go one level up, so we just pop element from stack and forgot about it.
# If we have any other element except several cases, we put it to the end of stack. So, what cases we need to avoid: if we meet ., it means current directory according to problem description, so we do not need to go deeper; if we meet .., and it means that stack is empty, so we already at the top of our path, so we againd do nothing in this case. Finally, we can meet empty string also, it corresponds to case, when we have //, then there is empty string between two /.
# In the end we reconstruct string from all element, using / to join them.
# Complexity: time complexity is O(n), because we only traverse our path once. Space complexity is O(n), because there can be potentially O(n) elements inside.