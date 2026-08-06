class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {

        auto max_iter = std::max_element(weights.begin(),weights.end());
        int lp = *max_iter;
        int rp = std::accumulate(weights.begin(),weights.end(),0);
        int min_weight_capacity = 25000000;
        while (lp <= rp)
        {
            int mp = floor((lp+rp)/2);
            int cumsum = 0;
            int count = 0;
            for (int i=0; i<weights.size(); i++)
            {
                if (cumsum + weights[i] <= mp)
                {
                    cumsum += weights[i];
                }
                else
                {
                    count += 1;
                    cumsum = weights[i];
                }
            }
            count += 1;
            if (count <= days)
            {
                rp = mp - 1;
                min_weight_capacity = std::min(min_weight_capacity,mp);
                
            }
            else
            {
                lp = mp + 1;
            }
        }
        return min_weight_capacity;
        
    }
};