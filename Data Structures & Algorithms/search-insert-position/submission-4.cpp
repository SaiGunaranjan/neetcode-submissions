class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

        int lp = 0;
        int rp = nums.size() - 1;

        if (target <= nums[lp])
        {
            return 0;
        }
        else if (target == nums[rp])
        {
            return rp;
        }
        else if (target > nums[rp])
        {
            return rp + 1;
        }

        while (lp <= rp)
        {
            int mid = floor((lp + rp) / 2);
            if (target == nums[mid])
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

        return rp + 1;
        
    }
};