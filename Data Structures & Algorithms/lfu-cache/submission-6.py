# Code on 29/08/2026
class ListNode:
    
    def __init__(self,key=None,value=None,freq=None,next=None,prev=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.next= next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):
        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.next = self.mru
        self.mru.prev = self.lru
        self.size = 0

class LFUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.key_node_map = {}
        self.freq_dll_map = {} # freq to doubly lunked list class mapping

    def update_links(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev 

    def update_mru(self,dll_obj, node):
        """
        Pass in the object of the corresponsing Doubly Linked List class and the node which has to be inserted into this doubly linked list
        """ 
        
        dll_obj.mru.prev.next = node
        node.prev = dll_obj.mru.prev
        node.next = dll_obj.mru
        dll_obj.mru.prev = node

        dll_obj.size += 1 # Update the size of the object of the corresponding Doubly Linked List by 1

    def get_freq_obj_update_mru(self,key,freq):

        if freq not in self.freq_dll_map:
            self.freq_dll_map[freq] = DoublyLinkedList()
        obj = self.freq_dll_map[freq]
        self.update_mru(obj,self.key_node_map[key])



    def update_node_pos(self,key):
        self.update_links(self.key_node_map[key])
        self.freq_dll_map[self.key_node_map[key].freq].size -= 1
        if self.key_node_map[key].freq == self.min_freq and self.freq_dll_map[self.key_node_map[key].freq].size == 0:
            self.min_freq += 1
        self.key_node_map[key].freq += 1 # It is about to go to next freq bucket

        self.get_freq_obj_update_mru(key,self.key_node_map[key].freq)
        
        


    def get(self, key: int) -> int:

        if key not in self.key_node_map:
            return -1
        else:
            self.update_node_pos(key)
            return self.key_node_map[key].value


        

    def put(self, key: int, value: int) -> None:
        
        if key in self.key_node_map:
            self.update_node_pos(key)
            self.key_node_map[key].value = value
        else:
            if len(self.key_node_map) < self.capacity:
                self.key_node_map[key] = ListNode(key=key,value=value,freq=1)
                self.min_freq = 1
                self.get_freq_obj_update_mru(key,self.min_freq)
            else:
                lfu_bucket_obj = self.freq_dll_map[self.min_freq]
                key_to_delete = lfu_bucket_obj.lru.next.key
				# Update lru for the min_freq obj
                lfu_bucket_obj.lru.next = lfu_bucket_obj.lru.next.next
                lfu_bucket_obj.lru.next.prev = lfu_bucket_obj.lru
                self.freq_dll_map[self.min_freq].size -= 1 # Reduce size of doubly linked list by 1 after removing the LFU + LRU node
                del self.key_node_map[key_to_delete] # delete the LFU + LRU key
                self.key_node_map[key] = ListNode(key=key,value=value,freq=1) # Create new node object
                self.min_freq = 1 # Reset min_freq to 1 when a new key is added
                self.get_freq_obj_update_mru(key,self.min_freq)





        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)