class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.q = []
        self.hash_map = {}
        

    def get(self, key: int) -> int:


        self.q = [ele for ele in self.q if ele != key]
        self.q.append(key)

        if key in self.hash_map:
            return self.hash_map[key]
        else:
            return -1

        
        

    def put(self, key: int, value: int) -> None:

        if len(self.hash_map) != self.capacity:

            self.q = [ele for ele in self.q if ele!=key]
            self.q.append(key)

            self.hash_map[key] = value
        
        else:
            if key in self.hash_map:
                self.q = [ele for ele in self.q if ele!=key]
                self.q.append(key)
                self.hash_map[key] = value
            else:
                lru_key = None
                ind = -1
                while lru_key is None:
                    ind += 1
                    lru_key = self.hash_map.pop(self.q[ind],None)
                
                self.q = [ele for ele in self.q if ele!=key]
                self.q.append(key)
                self.hash_map[key] = value


        
        
        

            

        
