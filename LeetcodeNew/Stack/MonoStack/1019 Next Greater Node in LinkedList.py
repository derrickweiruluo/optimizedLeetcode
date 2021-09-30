'''
You are given the head of a linked list with n nodes.
For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

EX1:
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]

EX2:
Input: head = [2,1,5]
Output: [5,5,0]

'''

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []  # increasing stack of [idx, curVal]
        res = []
        
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
                
            stack.append((len(res), head.val)) # len(res) is the idx of the node
            res.append(0)       # initialize to expand res, since in linkedList, size is unknown, expand after vistied each node
            head = head.next    # idxing to next node
        
        return res