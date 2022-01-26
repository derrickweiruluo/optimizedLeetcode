'''
Given the head of a singly linked list, return true if it is a palindrome.

'''


# Time: O(N), Space O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # find the mid node
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        #1->2->null :: 2->1->null
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        # compare the first and second half nodes
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        
        return True