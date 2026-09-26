class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.container = {}
        self.limit = capacity
        self.nodes = {}
        self.dummy = ListNode()
        self.tail = self.dummy

    def get(self, key: int) -> int:
        val = self.container.get(key, -1)
        
        if val != -1 and self.nodes[key].next:
            A = self.nodes[key].prev
            B = self.nodes[key]
            C = self.nodes[key].next

            A.next = C
            C.prev = A
            self.tail.next = B
            B.prev = self.tail
            B.next = None
            self.tail = B
            
        return val


    def put(self, key: int, value: int) -> None:
        if key not in self.container and len(self.container) == self.limit:
            del self.container[self.dummy.next.val]
            del self.nodes[self.dummy.next.val]
            self.dummy.next = self.dummy.next.next
            if not self.dummy.next:
                self.tail = self.dummy
            else:
                self.dummy.next.prev = self.dummy
            
        if key in self.nodes:
            if self.nodes[key].next:
                if self.nodes[key].next:
                    A = self.nodes[key].prev
                    B = self.nodes[key]
                    C = self.nodes[key].next
        
                    A.next = C
                    C.prev = A
                    self.tail.next = B
                    B.prev = self.tail
                    B.next = None
                    self.tail = B
        else:
            self.tail.next = ListNode(key, self.tail)
            self.tail = self.tail.next
            self.nodes[key] = self.tail
            print(self.tail.val)
        self.container[key] = value