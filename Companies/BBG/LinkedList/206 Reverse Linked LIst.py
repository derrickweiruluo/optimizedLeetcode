


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev
        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            curNext = cur.next
            cur.next = prev
            prev, cur = cur, curNext
        
        return prev