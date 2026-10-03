# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node_map = defaultdict(list)
        for head in lists:
            while head:
                node_map[head.val].append(head)
                head = head.next
        new_head = curr = ListNode()
        for nodes in sorted(node_map.keys()):
            for node in node_map[nodes]:
                if curr:
                    curr.next = node
                    curr = curr.next
                else:
                    curr = node
                    new_head = curr
        return new_head.next 