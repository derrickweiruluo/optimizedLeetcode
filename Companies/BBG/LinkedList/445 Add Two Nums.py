''''

7 --> 2 --> 4 --> 3
      5 --> 6 --> 4


return  # 7243 + 564 = 7807  input output 都是正着来
7 --> 8 --> 0 --> 7

'''

# return  # 7243 + 564 = 7807  input output 都是正着来
# 7 --> 8 --> 0 --> 7
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        x1 = x2 = 0
        while l1:
            x1, l1 = x1 * 10 + l1.val, l1.next
        while l2:
            x2, l2 = x2 * 10 + l2.val, l2.next
        x = x1 + x2
        if not x: return Node(0)
        
        cur, prev = None, None
        while x > 0:
            cur = Node(x % 10)
            cur.next = prev
            prev = cur
            x //= 10
        
        return cur



# BAD, two stack solutions
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry, head = 0, None
        
        
        while stack1 or stack2 or carry:
            d1 = stack1.pop() if stack1 else 0
            d2 = stack2.pop() if stack2 else 0
            carry, cur_val = divmod(d1 + d2 + carry, 10)
            # head_new = ListNode(cur_val)
            # head_new.next = head
            # head = head_new
            
            # The cleanest way to write and update head pointer is:
            head = ListNode(cur_val, head)
        
        return head