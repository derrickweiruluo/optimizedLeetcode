
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head: return None

        # Step 1: 计算LinkedList的长度，链接head and tail
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        k = k % length
        cur.next = head
        
        # step 2: Advance the head to new head's PREV
        cur2 = head
        for _ in range(length - k - 1):
            cur2 = cur2.next
        

        # Step 3: break the new tail and new head's connection
        newHead = cur2.next
        cur2.next = None
        return newHead