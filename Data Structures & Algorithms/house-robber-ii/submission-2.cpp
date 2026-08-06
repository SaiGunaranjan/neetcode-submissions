class Solution {
public:
    int rob(vector<int>& nums) {

        if (nums.size() == 1)
        {
            return nums[0];
        }

        if (nums.size() == 2)
        {
            return std::max(nums[0], nums[1]);
        }

        int l = nums.size() - 1;
        vector<int> max_amount_1(l,0);
        vector<int> max_amount_2(l,0);

        max_amount_1[0] = nums[0];
        max_amount_1[1] = std::max(nums[0],nums[1]);

        max_amount_2[0] = nums[1];
        max_amount_2[1] = std::max(nums[1],nums[2]);

        for (int i=2; i<l; i++)
        {
            max_amount_1[i] = std::max(max_amount_1[i-2]+ nums[i], max_amount_1[i-1]);
            max_amount_2[i] = std::max(max_amount_2[i-2]+ nums[i+1], max_amount_2[i-1]);
        }
        
        return std::max(max_amount_1[l-1],max_amount_2[l-1]);
    }
};
