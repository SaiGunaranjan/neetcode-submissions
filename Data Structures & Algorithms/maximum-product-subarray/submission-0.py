class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_prod = -10000
        for i in range(len(nums)):
            prod = 1
            for j in range(i,len(nums)):
                prod *= nums[j]
                if prod > max_prod:
                    max_prod = prod

        return max_prod

        