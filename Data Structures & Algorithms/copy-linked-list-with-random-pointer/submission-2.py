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
        map1 = {}
        map2 = {}
        dummy = Node(0)
        new_node = dummy

        node = head
        indx = 0
        while node:
            map1[node] = indx
        
            new_node.next = Node(node.val) 
            new_node = new_node.next
            map2[indx] = new_node

            indx += 1
            node = node.next

        map1[node] = indx
        map2[indx] = None
        
        new_list_head = dummy.next       
        new_node = new_list_head
        node = head
        while node:
            indx = map1[node.random]
            new_node.random = map2[indx]

            node = node.next
            new_node = new_node.next

        return new_list_head
        