"""
Given the head of a singly linked list, reverse the list, and return the reversed list.


###
EASY 基操
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  # iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        return prev

class Solution: # recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev
