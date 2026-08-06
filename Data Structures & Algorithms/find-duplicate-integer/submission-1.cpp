class Solution {
public:
    int findDuplicate(vector<int>& nums) {

        std::unordered_map<int,int> freq_dict;
        for (int i = 0; i < nums.size(); i++)
        {
            if (freq_dict.find(nums[i]) != freq_dict.end())
            {
                return nums[i];
            }
            else
            {
                freq_dict[nums[i]] = 1;
            }
        }
        
    }
};
