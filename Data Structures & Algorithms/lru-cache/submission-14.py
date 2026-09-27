class ListNode:
    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.limit = capacity
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.keys:
            self.move(self.keys[key])
            return self.keys[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.keys and len(self.keys) == self.limit:
            del self.keys[self.left.next.key]
            self.remove()

            
        if key in self.keys:
            self.keys[key].val = value
            self.move(self.keys[key])
        else:
            node = ListNode(key, value)
            self.keys[key] = node
            self.insert(node)
            


    def insert(self, node):       
        # insert at right
        A = self.right.prev
        B = node
        C = self.right
        A.next = B
        B.prev = A
        B.next = C
        C.prev = B
    
    def move(self, node):
        if node.next != self.right:
            A = node.prev
            B = node
            C = B.next
            A.next = C
            C.prev = A
            B.prev = self.right.prev
            self.right.prev.next = B
            B.next = self.right
            self.right.prev = B

    def remove(self):
        A = self.left
        C = self.left.next.next
        A.next = C
        C.prev = A