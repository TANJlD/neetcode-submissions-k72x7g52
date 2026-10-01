# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return 
            
        fast = slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        head2 = prev.next
        prev.next = None

        
        prev = head2
        curr = head2.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        head2.next = None
        head2 = prev
        
        curr = head
        while curr.next:
            nxt = curr.next
            curr.next = head2
            head2 = head2.next
            curr.next.next = nxt
            curr = nxt
        
        curr.next = head2

        
        
        
        

        