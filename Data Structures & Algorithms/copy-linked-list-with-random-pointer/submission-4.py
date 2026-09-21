"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        dummy = new_node = Node(0)
        node = head
        while node:
            new_node.next = Node(node.val)
            new_node = new_node.next
            map[node] = new_node
            node = node.next

        node = head
        new_list = new_node = dummy.next
        while new_node:
            new_node.random = map.get(node.random, None)
            node = node.next
            new_node = new_node.next

        return new_list
