class MyHashSet:

    class Node:
        def __init__(self):
            self.val = None
            self.next_node = None

    def __init__(self):
        self.head = self.Node()
        

    def add(self, key: int) -> None:

        if self.head.next_node is None:
            new_node = self.Node()
            new_node.val = key
            self.head.next_node = new_node
            return

        curr_node = self.head.next_node
        
        while curr_node is not None:
            if curr_node.val == key:
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next_node
        
        new_node = self.Node()
        new_node.val = key
        prev_node.next_node = new_node
        

    def remove(self, key: int) -> None:

        if self.head.next_node is None:
            return
        curr_node = self.head.next_node
        prev_node = self.head
        while curr_node is not None:
            if curr_node.val == key:
                prev_node.next_node = curr_node.next_node
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next_node



        

    def contains(self, key: int) -> bool:

        if self.head.next_node is None:
            return False
        
        curr_node = self.head.next_node
        while curr_node is not None:
            if curr_node.val == key:
                return True
            else:
                curr_node = curr_node.next_node
        
        return False