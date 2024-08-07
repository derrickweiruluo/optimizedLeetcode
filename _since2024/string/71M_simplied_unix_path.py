"""
Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.


Conditions:
1. Must start with a single slash '/'.
2. Directories within the path should be separated by only one slash '/'.
3. It should not end with a slash '/', unless it's the root directory.
4. It should exclude any single or double periods used to denote current or parent directories.


Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: The trailing slash should be removed.

Example 2:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation:  Multiple consecutive slashes are replaced by a single one.

Example 3:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:  A double period ".." refers to the directory up a level.

Example 4:
Input: path = "/../"
Output: "/"
Explanation:  Going one level up from the root directory is not possible.

Example 5:
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation:  "..." is a valid name for a directory in this problem.
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        # https://leetcode.com/submissions/detail/607772098/
        # with explanation

        stack = []
        for _dir in path.split("/"):
            if stack and _dir == "..":  # condition_1 for poping directory
                stack.pop()
            elif _dir not in [".", "", ".."]:  # condition_3 for appending directory
                stack.append(_dir)
            # skipping condition_3 if empty stack and _dir == "..", which is invalid moving up
        return "/" + "/".join(stack)
