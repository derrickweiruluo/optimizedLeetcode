"""
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them


Example 1:

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]



Foreword
I saw some solutions saying O(N) time, but actually they are not.
If it takes already O(N) time to find left part and right part, it could not be O(N).


Complexity:
Time O(N), as we iterate both pre index and post index only once.
Space O(height), depending on the height of constructed tree.


Recursive Solution
Create a node TreeNode(pre[preIndex]) as the root.

Becasue root node will be lastly iterated in post order,
if root.val == post[posIndex],
it means we have constructed the whole tree,

If we haven't completed constructed the whole tree,
So we recursively constructFromPrePost for left sub tree and right sub tree.

And finally, we'll reach the posIndex that root.val == post[posIndex].
We increment posIndex and return our root node.
"""


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.pre_idx = self.post_idx = 0
        
        def build():
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            
            if root.val != postorder[self.post_idx]:
                root.left = build()
            if root.val != postorder[self.post_idx]:
                root.right = build()
            
            self.post_idx += 1
            return root
        
        return build()
