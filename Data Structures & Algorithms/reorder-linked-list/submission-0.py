# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = {}

        curr = head
        indx = 0
        while curr:
            nodes[indx] = curr
            indx += 1
            curr = curr.next

        curr = head
        l = 1
        r = indx - 1
        count = 0
        while l <= r:  
            if not count % 2:
                curr.next = nodes[r]
                curr = curr.next
                r -= 1 
            else:
                curr.next = nodes[l]
                curr = curr.next
                l += 1
            count += 1
        curr.next = None
        
