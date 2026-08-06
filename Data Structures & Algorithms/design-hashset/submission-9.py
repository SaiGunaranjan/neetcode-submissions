class MyHashSet:
    
    class Node:
        def __init__(self,val):
            self.val = val
            self.next_node = None

    def __init__(self):
        self.head = None
        
        

    def add(self, key: int) -> None:
        if self.head is None:
            self.head = self.Node(key)
            return
        curr_node = self.head
        while curr_node.next_node is not None:
            if curr_node.val == key:
                return
            else:
                curr_node = curr_node.next_node
        
        if curr_node.val == key:
            return
        else:
            curr_node.next_node = self.Node(key)
        

    def remove(self, key: int) -> None:

        if self.head is None:
            return
        dummy_node = self.Node(0)
        dummy_node.next_node = self.head
        prev_node = dummy_node
        curr_node = self.head
        while curr_node.next_node is not None:
            if curr_node.val == key:
                prev_node.next_node = curr_node.next_node
                self.head = dummy_node.next_node
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next_node
        
        if curr_node.val == key:
            prev_node.next_node = curr_node.next_node
        self.head = dummy_node.next_node


        

    def contains(self, key: int) -> bool:

        if self.head is None:
            return False
        
        curr_node = self.head
        while curr_node.next_node is not None:
            if curr_node.val == key:
                return True
            else:
                curr_node = curr_node.next_node
        
        if curr_node.val == key:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)