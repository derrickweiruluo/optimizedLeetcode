'''
Input: head = [2,1,5]
Output: [5,5,0]


Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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