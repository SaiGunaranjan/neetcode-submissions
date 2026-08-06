class MyCircularQueue {

private:
    std::vector<int> q = {};
    int k;
   
public:
    MyCircularQueue(int k): k(k) {
         
    }
    
    bool enQueue(int value) {

        if (q.size() != k)
        {
            q.push_back(value);
            return true;
        }
        else
        {
            return false;
        }
        
    }
    
    bool deQueue() {
        
        if (q.size() != 0)
        {
            q.erase(q.begin());
            return true;
        }
        else
        {
            return false;
        }
        
    }
    
    int Front() {
        
        if (q.size() != 0)
        {
            return q[0];
        }
        else
        {
            return -1;
        }
        
    }
    
    int Rear() {

        int q_size = q.size();
        if (q_size != 0)
        {
            return q[q_size-1];
        }
        else
        {
            return -1;
        }
        
    }
    
    bool isEmpty() {

        return q.size() == 0;
        
    }
    
    bool isFull() {

        return q.size() == k;
        
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */