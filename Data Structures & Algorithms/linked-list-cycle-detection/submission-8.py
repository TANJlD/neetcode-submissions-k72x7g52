# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# What would be the base case for a recursive solution of this problem ?? 
# Let's imagine we are traversing through two Lists, if we hit the same elements,
# we activate the return statement 

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        if not fast or not fast.next or not fast.next.next:
            return False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False