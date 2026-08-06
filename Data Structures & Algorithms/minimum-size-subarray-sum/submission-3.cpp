class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {

        int n = nums.size();
        int lp = 0;
        int rp = 0;
        int sum_arr = nums[0];
        int min_subarr_len = 100000;
        while (lp < n && rp < n)
        {
            if (sum_arr >= target)
            {
                if (lp == rp)
                {
                    return 1;
                }
                min_subarr_len = min(min_subarr_len,rp-lp+1);
                sum_arr -= nums[lp];
                lp += 1;
            }
            else
            {
                rp += 1;
                if (rp > n-1)
                {
                    break;
                }
                sum_arr += nums[rp];
            }
        }
        if (rp - lp >= n)
        {
            return 0;
        }
        return min_subarr_len;
        
    }
};