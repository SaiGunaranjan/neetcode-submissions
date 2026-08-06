class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        l = len(nums) - 1
        max_amount_1 = [-1]*l
        max_amount_2 = [-1]*l

        max_amount_1[0] = nums[0]
        max_amount_1[1] = max(nums[1], nums[0])

        max_amount_2[0] = nums[1]
        max_amount_2[1] = max(nums[1],nums[2])

        for i in range(2,l):
            max_amount_1[i] = max(max_amount_1[i-2]+nums[i], max_amount_1[i-1])
            max_amount_2[i] = max(max_amount_2[i-2]+nums[i+1], max_amount_2[i-1])
        
        return max(max_amount_1[-1],max_amount_2[-1])
        