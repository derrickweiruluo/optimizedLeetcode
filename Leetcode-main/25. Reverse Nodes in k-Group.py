# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return null
        
        dummy = ListNode(-1)
        dummy.next = head
        curr, nextStart = dummy, dummy.next
        
        # 用stack的后进先出来reserve linkedlist
        stack = []
        
        while nextStart:
            for i in range(k):
                stack.append(nextStart)
                nextStart = nextStart.next
                if not nextStart: break
            
            if len(stack) < k: return dummy.next
            
            while stack:
                curr.next = stack.pop()
                curr = curr.next
            
            # 当stack pop完为空时
            curr.next = nextStart
        
        return dummy.next
