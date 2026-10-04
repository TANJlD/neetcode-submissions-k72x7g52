class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head: return None
        curr = head
        l = 1
        while curr.next and l < k:
            curr = curr.next
            l += 1
        
        rest = curr.next
        curr.next = None
    
        if l < k:
            return head
        else:
            rev_head = self.reverse(head)
            head.next = self.reverseKGroup(rest, k)
            return rev_head


    def reverse(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev