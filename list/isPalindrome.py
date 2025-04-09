import ListNode

class Solution:
    
    def findMiddle(self, head:ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self, head:ListNode) -> ListNode:
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        middle = self.findMiddle(head)
        head2 = self.reverse(middle)

        while head2:
            if (head2.val != head.val):
                return False
            head2 = head2.next
            head = head.next
        return True
