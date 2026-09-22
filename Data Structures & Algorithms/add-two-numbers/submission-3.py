# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # sum = val1 + val2 + remainder
        # remainder = sum % 10
        # add = sum - remainder

        dummy = new_node = ListNode(0)

        node1, node2 = l1, l2
        first = 0
        while node1 or node2:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            
            total = val1 + val2 + first
            first = total // 10
            last = total % 10

            new_node.next = ListNode(last)

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
            new_node = new_node.next

        if first: 
            new_node.next = ListNode(first)

        return dummy.next


