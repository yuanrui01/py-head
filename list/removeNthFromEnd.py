class Solution:
    # 19. 删除链表的倒数第 N 个结点
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        for i in range(n):
            head = head.next
        
        while (head):
            head = head.next
            p = p.next
        p.next = p.next.next
        return dummy.next