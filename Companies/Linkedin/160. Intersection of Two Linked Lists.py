"""
https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49838/5-line-python-solution
https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49938/Python-Solution%3A-O(n)-time-and-O(1)-space
https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/50010/My-concise-python-solution-run-in-O(n)-time-and-O(1)-memory
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
begin to intersect at node c1.
Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8
(note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B,
it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B.
"""

#解法：node1 = node1.next if node else headB
# 一个链走到尽头的时候，停顿一个回合，然后嫁接到另一条链子head
# 两条都可以这样操作，取决于长短，因为有停顿，最终会同时到达intersection
# 

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while node1 != node2:
            # print(node1 == None)
            # print(node1.val, node2.val)
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        
        return node1
        
        
        #下面的解释有问题
        # 非常妙！ O(1)space and worst case O(N + M) time
        # loop 完两个链，链1尾连链2头，反之亦然
        
        while d1 != d2:
            print(d1 == None)
            print(d1.val, d2.val)
            d1 = d1.next if d1 else headB 
            d2 = d2.next if d2 else headA
            
        # 这一步最精妙的是，当d1 d2 同时走完两条链子，都指向None时：
        #     d1 == d2, 中断while loop，返回任意一个都是None
        return d1
            
        
                