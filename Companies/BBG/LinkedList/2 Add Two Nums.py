'''
2 --> 4 --> 3
5 --> 6 --> 4


return  342 + 465 = 807 反着来
7 --> 0 --> 8
'''

# 342 + 465 = 807 反着来， 结果return  7--0--8
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = cur = ListNode(0)
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            carry, val = divmod(carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
        
        return dummy.next