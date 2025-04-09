import ListNode

# 876. 链表的中间结点
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast  = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow