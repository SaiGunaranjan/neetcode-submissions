class DoubleListNode:
    def __init__(self,key=None,val=None,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.lru = self.mru = DoubleListNode()


    def update_link(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def update_mru(self, node):
        self.mru.prev.next = node
        node.prev = self.mru.prev
        node.next = self.mru
        self.mru.prev = node
    
    def update_lru(self):
        self.lru.next = self.lru.next.next
        self.lru.next.prev = self.lru

    def get(self, key: int) -> int:

        if key in self.hash_map:
            self.update_link(self.hash_map[key])
            self.update_mru(self.hash_map[key])
            return self.hash_map[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.hash_map:
            self.update_link(self.hash_map[key])
            self.update_mru(self.hash_map[key])
            self.hash_map[key].val = value
        else:
            if len(self.hash_map) == 0:
                self.hash_map[key] = DoubleListNode(key=key,val=value)
                self.lru.next = self.hash_map[key]
                self.hash_map[key].prev = self.lru
                self.mru.prev = self.hash_map[key]
                self.hash_map[key].next = self.mru
            elif len(self.hash_map) > 0 and len(self.hash_map) < self.capacity:

                self.hash_map[key] = DoubleListNode(key=key, val=value)
                self.update_mru(self.hash_map[key])
            else:
                key_to_del = self.lru.next.key
                self.update_lru()
                del self.hash_map[key_to_del]
                self.hash_map[key] = DoubleListNode(key=key, val=value)
                self.update_mru(self.hash_map[key])


    


                



        
