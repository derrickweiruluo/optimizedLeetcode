"""
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev, cur = cur, cur_next
        return prev
