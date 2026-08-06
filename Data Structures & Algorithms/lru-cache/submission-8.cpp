#include <optional>
class LRUCache {
private:
    int capacity;
    std::unordered_map<int, int> hash_map;
    std::vector<int> q;

public:
    LRUCache(int capacity): capacity(capacity) {

    }
    
    int get(int key) {

        q.erase(remove(q.begin(), q.end(), key), q.end());
        q.push_back(key);
        
        if (hash_map.find(key) != hash_map.end())
        {
            return hash_map[key];
        }
        else
        {
            return -1;
        }
        
    }
    
    void put(int key, int value) {

        if (hash_map.size() == capacity)
        {
            if (!(hash_map.find(key) != hash_map.end()))
            {
                std::optional<int> lru_key;
                int ind = -1;
                while (!(lru_key.has_value()))
                {
                    ind += 1;
                    if (hash_map.count(q[ind]))
                    {   
                        lru_key = q[ind];
                        hash_map.erase(q[ind]);
                    }
                }
            }
        }
        q.erase(remove(q.begin(), q.end(), key), q.end());
        q.push_back(key);
        hash_map[key] = value;
        
    }
};
