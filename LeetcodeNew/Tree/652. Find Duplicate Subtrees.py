
# We can serialize subtrees while traversing the tree, and then compare the serializations to see if there are duplicates.
# The post-order traversal is natural here.
# As for the construction of the serialization string, we can apply either the pre-order or the post-order. 
# The in-order is inappropriate here because trees as shown below will have the same serializations if in-order.

#    0
#   /
#  0

#  0
#   \
#    0
# Since we only need to return the root node of any one of duplicate subtrees of the same kind, we utilize a dictionary that maps a serialization string to its appearances. And we add a subtree root to result only if its serialization string appears once.

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        ## Post order traversal
        
        res = []
        serial_cnt = {}
        self.encode(root, res, serial_cnt)
        return res
    
    def encode(self, node, res, serial_cnt) -> str:
        if not node:
            return ""
        
        # serializing step, add spacers between root, left and right
        # the original code will fail on new test case: [2,1,11,11,null,1], 
        # this is because str(11) = str(1) == str(1) + str(11)
        serial = str(node.val) + "." + self.encode(node.left, res, serial_cnt) + "," + self.encode(node.right, res, serial_cnt)
        serial_cnt[serial] = serial_cnt.get(serial, 0) + 1
        
        # count for this serialized tree, whether is duplicate
        if serial_cnt[serial] == 2:
            res.append(node)
        
        return serial
