class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2 != 0:
            return False

        half_sum = sum(nums)//2
        sum_val = 0

        def half_sum_subset(ind,subsum):

            if ind == len(nums)-1:
                return subsum==half_sum
            else:
                return half_sum_subset(ind+1,subsum+nums[ind+1]) or half_sum_subset(ind+1,subsum)
                   
        
        
        return half_sum_subset(0,sum_val+nums[0]) or half_sum_subset(0,sum_val)