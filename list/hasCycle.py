class Solution:
    # 141. 环形链表
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                return True
        return False