#class Node:
#    def __init__(self,val=None,next_ptr=None):
#        self.val = val
#        self.next_ptr = next_ptr
class MyCircularQueue:

    def __init__(self, k: int):

        self.k = k
        self.circ_q_list = [None]*self.k
        self.front_ptr = None
        self.rear_ptr = None
    
    def mod(self,value,k):

        if value>=k:
            return value-k
        elif value < 0:
            return value+k
        else:
            return value

        

    def enQueue(self, value: int) -> bool:

        if self.front_ptr is None:
            self.circ_q_list[0] = value
            self.front_ptr = self.rear_ptr = 0
            return True

        if self.mod(self.rear_ptr - self.front_ptr,self.k) == self.k-1:
            return False
        else:
            self.rear_ptr = self.mod(self.rear_ptr+1,self.k)
            self.circ_q_list[self.rear_ptr] = value
            return True



        


        
        

    def deQueue(self) -> bool:

        if self.front_ptr is None:
            return False
        
        self.circ_q_list[self.front_ptr] = None
        self.front_ptr = self.mod(self.front_ptr+1,self.k)
        if (self.mod(self.front_ptr-self.rear_ptr,self.k) == 1) or (self.circ_q_list[self.rear_ptr] is None):
            # Circular Que has completely emptied and so reset the front and rear pointers
            self.front_ptr = None
            self.rear_ptr = None
        return True
        

    def Front(self) -> int:
        if self.front_ptr is None:
            return -1
        else:
            return self.circ_q_list[self.front_ptr]
        

    def Rear(self) -> int:

        if self.rear_ptr is None:
            return -1
        else:
            return self.circ_q_list[self.rear_ptr]
        

    def isEmpty(self) -> bool:
        if self.front_ptr is None:
            return True
        else:
            return False
        

    def isFull(self) -> bool:

        if self.mod(self.rear_ptr-self.front_ptr,self.k) == self.k - 1:
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