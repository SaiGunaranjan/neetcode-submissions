class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)== 1:
            return nums[0]
        max_amount_robbed = [-1]*len(nums)
        max_amount_robbed[0] = nums[0]
        max_amount_robbed[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            max_amount_robbed[i] = max(max_amount_robbed[i-2] + nums[i], max_amount_robbed[i-1])
        
        return max_amount_robbed[-1]