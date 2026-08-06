class Solution {
public:
    int rob(vector<int>& nums) {

        int len_nums = nums.size();
        if (len_nums == 1)
        {
            return nums[0];
        }

        std::vector<int> max_amount_robbed(len_nums,0);
        max_amount_robbed[0] = nums[0];
        max_amount_robbed[1] = std::max(nums[0],nums[1]);
        for (int i=2; i<len_nums; i++ )
        {
            max_amount_robbed[i] = std::max(max_amount_robbed[i-2] + nums[i], max_amount_robbed[i-1]);
        }
        return max_amount_robbed[len_nums-1];
        
    }
};
