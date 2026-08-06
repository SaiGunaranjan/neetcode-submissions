class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_prod = -11
        f_prod = 1
        b_prod = 1
        for i in range(len(nums)):
            f_prod *= nums[i]
            b_prod *= nums[len(nums)-i - 1]
            max_prod = max(max_prod,f_prod,b_prod)
            if f_prod == 0:
                f_prod = 1
            if b_prod == 0:
                b_prod = 1

        return max_prod
        