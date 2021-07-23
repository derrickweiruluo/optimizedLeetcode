# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        dummy = ListNode(-1)
        dummy.next = head
        
        prev_slow = prev_fast = dummy
        slow = fast = head
        
        for i in range(k - 1): #停泊正K th的nodes: slow 和他的slow_fast
            prev_slow = slow
            slow = slow.next
        
        null_checker = slow
        
        while null_checker.next: #停泊反K th的nodes: fast 和他的prev_fast
            prev_fast = fast
            fast = fast.next
            null_checker = null_checker.next
            
        if slow == fast: return head
        
        # 一下子这一步是4个pointer的操作，先操作prev.next，在操作target.next
        prev_slow.next, prev_fast.next = fast, slow
        slow.next, fast.next = fast.next, slow.next

        
        return dummy.next
