"""
original: 1 -> (2 -> 3 -> 4) -> 5
reversed: 1 -> (4 -> 3 -> 2) -> 5
left = 2, right = 4
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre_head = ListNode(-500, head)  # 这一步是绝对reference node for return only
        prev, cur = pre_head, head

        # step 1: advancing cur to the first node 
        for _ in range(left - 1):  # indexing n is important (requirement)
            prev = prev.next
            cur = cur.next

        # step 2: swaping node like below
        """
        1->3->2->4->5
        1->4->3->2->5
        """
        for _ in range(right - left): # amount is also important (requirement)
            cur_next = cur.next
            cur.next = cur_next.next
            cur_next.next = prev.next
            prev.next = cur_next

        return pre_head.next
