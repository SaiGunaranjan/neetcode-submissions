class Solution {
public:
    int search(vector<int>& nums, int target) {

        int lp = 0;
        int rp = nums.size() - 1;
        int mid;

        while (lp <= rp)
        {
            mid = floor((lp + rp) / 2);

            if  (target == nums[mid])
            {
                return mid;
            }
            else if (target < nums[mid])
            {
                rp = mid - 1;
            }
            else
            {
                lp = mid + 1;
            }
        
        }
        return -1;
        
    }
};
