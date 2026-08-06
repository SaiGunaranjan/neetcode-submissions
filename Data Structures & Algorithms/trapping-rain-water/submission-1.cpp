class Solution {
public:
    int trap(vector<int>& height) {

        int len_arr = height.size();
        vector<int> max_height_left = {};
        vector<int> max_height_right = {};

        int left_max = 0;
        for (int val: height)
        {
            left_max = std::max(left_max,val);
            max_height_left.push_back(left_max);
        }

        int right_max = 0;
        for (int i = len_arr-1; i > -1; i--)
        {
            right_max = std::max(right_max,height[i]);
            max_height_right.push_back(right_max);
        }

        int water_stored = 0;
        for (int i = 0; i < len_arr; i++)
        {
            int limit_height = std::min(max_height_left[i], max_height_right[len_arr-i-1]);
            if (limit_height > height[i])
            {
                water_stored += (limit_height - height[i]);
            }
        }
        return water_stored;

        
    }
};
