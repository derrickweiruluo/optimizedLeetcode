"""
Example:
Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
    4
   / \
  2   5
 / \
1   3
Output: [4,3]
Follow up:
Assume that the BST is balanced,
could you solve it in less than O(n) runtime (where n = total nodes)?
https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70556/Simple-DFS-%2B-Priority-Queue-Python-Solution
https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70573/Clear-Python-O(klogn)-Solution-with-Two-Stacks
Step 1. Binary search for target until node==None or node.val == target, record path
Step 2. For path node, if node.val>=target, add to stack Pred; otherwise(node.val<=target) add to stack Succ
Step 3. Stack tops are possible nearest element
Step 4. Compare both stack for nearest element and then "iterate" the stack
一开始思路非常不明确，看了不少discuss也不明白为什么。在午饭时间从头仔细想了一下，
像Closest Binary Search Tree Value I一样，追求O(logn)的解法可能比较困难，
但O(n)的解法应该不难实现。我们可以使用in-order的原理，从最左边的元素开始，
维护一个Deque或者doubly linked list，将这个元素的值从后端加入到Deque中，然后继续遍历下一个元素。
当Deque的大小为k时， 比较当前元素和队首元素与target的差来尝试更新deque。
循环结束条件是队首元素与target的差更小或者遍历完全部元素。这样的话时间复杂度是O(n)， 空间复杂度应该是O(k)。
Time Complexity - O(n)， Space Complexity - O(k)
"""


'''
我的思路
inorder 从小到大遍历
target= 3.7， 快= 2
12345 里面，34是解，第一个不是解是5，他的root的右边将会被该root的return skip掉
which is 6's root subtree

Example:
Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
       4
     /    \
    2      6
   / \    / \
  1   3  5   8
            / \
           7   10   
Input: target = 3.714286, and k = 2
Output: [4,3]. searched 12345, 5's root is 6, 6's right subtree skipped

Input: target = 2.2, and k = 2
Output: [2,3. searched 123, 3's root is 4, 4's right subtree skipped
'''

# Definition for a binary tree node.
import collections
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        res = collections.deque([])
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            print(root.val)
            if len(res) == k:
                if abs(root.val - target) < abs(res[0] - target):
                    res.popleft()
                else:
                    return
            res.append(root.val)    
            inorder(root.right)
        
        inorder(root)
        return res