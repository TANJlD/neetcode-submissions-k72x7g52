class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        node = target = prev = head
        count = 0
        while node:
            if count >= n:
                prev = target
                target = target.next
            count += 1
            node = node.next
        if count == n:
            return head.next
        prev.next = target.next
        return head