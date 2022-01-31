'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        res = cur = ListNode(0)
        # print(l1.val, l2.val)
        
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
        
        return res.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = l1.val + l2.val
        digit, tenth = cur % 10, cur // 10
        root = ListNode(digit)
        if any((l1.next, l2.next, tenth)):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += tenth
            root.next = self.addTwoNumbers(l1, l2)    
        return root



