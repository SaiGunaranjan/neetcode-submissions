class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.dummy = Node()
        self.rear = self.dummy
        

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False
        else:
            self.rear.next = Node(val=value)
            self.rear = self.rear.next
            self.size += 1
            if self.size == 1:
                self.dummy.next = self.rear
            return True

        
        

    def deQueue(self) -> bool:
        
        if self.isEmpty():
            return False
        else:
            self.dummy.next = self.dummy.next.next
            self.size -= 1
            return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.dummy.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.rear.val
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()