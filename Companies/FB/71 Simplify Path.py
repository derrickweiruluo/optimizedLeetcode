'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.


In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
'''



'''Clarification:w
The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path

format of periods such as '...' are treated as file/directory names
'''



path = '/..'
path = '//'
path = '/...'
path = '/./../...////'

# 多个/// 被视为一个，三个点或以上是valid path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for directory in path.split("/"):
            if stack and directory == "..":
                stack.pop()
            else:
                # 当不再：当前dir '.', //导致的空白char, '..'
                if directory not in [".", "", ".."]:
                    stack.append(directory)
        
        return '/' + '/'.join(stack)
    
    
# When you see this problem, you should think about stack. Why? Because we have directories and you can go deeper or come back and when you come back, you basically forgot about all element after and stack is ideal simulation of this process. Also in python you can use .split("/") function, which will split our string into parts, separated by / symbol.

# So, the algorithm will look like this:

# If stack is not empty and we meet .. element, it means, that we need to go one level up, so we just pop element from stack and forgot about it.
# If we have any other element except several cases, we put it to the end of stack. So, what cases we need to avoid: if we meet ., it means current directory according to problem description, so we do not need to go deeper; if we meet .., and it means that stack is empty, so we already at the top of our path, so we againd do nothing in this case. Finally, we can meet empty string also, it corresponds to case, when we have //, then there is empty string between two /.
# In the end we reconstruct string from all element, using / to join them.
# Complexity: time complexity is O(n), because we only traverse our path once. Space complexity is O(n), because there can be potentially O(n) elements inside.