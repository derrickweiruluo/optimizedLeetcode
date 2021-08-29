"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]

Constraints:
The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
 

Follow-up: Can you solve the problem in O(1) extra memory space?

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head: return None
        
        dummy = ListNode(-1, head)
        prev, cur = dummy, head
        stack = []
        
        while cur:
            # step 1: 组建stack to be reversed, break if cur is NULL
            for i in range(k):
                stack.append(cur)
                cur = cur.next
                if not cur:
                    break
            # 如果当前尾巴组不够k个，返回结果
            if len(stack) < k:
                return dummy.next
            
            # prev pointer 来完成对掉工作with stack,一旦完成 prev = cur, 
            # where cur is the next starting pos to be reversed
            while stack:
                prev.next = stack.pop()
                prev = prev.next
            
            prev.next = cur
        
        return dummy.next
