# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        half = length // 2
        curr = head
        while half:
            curr = curr.next
            half -= 1
        next = curr.next
        curr.next = None
        curr = next

        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        list2 = prev

        curr = head
        list1 = head.next
        while list1 and list2:
            if curr.next == list1:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            else:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            
    
        curr.next = list1 or list2
