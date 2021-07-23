# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(-1)
        dummy.next = head
        
        fast = slow = dummy
        
        # 这道题关键在于用两个指针，且推断出要offset的距离，最好拿张纸画一画
        # Fast 存在的意义是让slow停在要被去除的node的前一个
        for i in range(n):
            fast = fast.next
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        # skip the target node
        slow.next = slow.next.next
        
        return dummy.next
