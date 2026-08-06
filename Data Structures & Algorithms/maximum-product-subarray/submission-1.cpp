class Solution {
public:
    int maxProduct(vector<int>& nums) {

        int max_prod = -10000;
        for (int i=0; i<nums.size(); i++)
        {
            int prod = 1;
            for (int j=i; j<nums.size();j++)
            {
                prod = prod * nums[j];
                if (prod > max_prod)
                {
                    max_prod = prod;
                }
            }
        }
        return max_prod;
    }
};
