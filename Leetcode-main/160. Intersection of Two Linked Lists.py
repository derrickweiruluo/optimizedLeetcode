# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d1, d2 = headA, headB
        
        # 非常妙！ O(1)space and worst case O(N + M) time
        # loop 完两个链，链1尾连链2头，反之亦然
        
        while d1 != d2:

            d1 = d1.next if d1 else headB 
            d2 = d2.next if d2 else headA
            
        # 这一步最精妙的是，当d1 d2 同时走完两条链子，都指向None时：
        #     d1 == d2, 中断while loop，返回任意一个都是None
        return d1
            
        
                
