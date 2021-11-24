
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
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        
        res = temp.next

        # Step 3: break the new tail and new head's connection
        temp.next = None
        return res