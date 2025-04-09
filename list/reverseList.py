import ListNode

class Solution:
    # 206. 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre