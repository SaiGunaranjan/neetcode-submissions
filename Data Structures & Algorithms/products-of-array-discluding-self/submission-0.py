class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_arr = len(nums)
        prefix_prod_arr = [1]
        suffix_prod_arr = [1]
        prod_arr = []

        prefix_prod = 1
        for ind in range(1,len_arr):
            prefix_prod *= nums[ind-1]
            prefix_prod_arr.append(prefix_prod)

        
        suffix_prod = 1
        for ind in range(len_arr-2,-1,-1):
            suffix_prod *= nums[ind+1]
            suffix_prod_arr.append(suffix_prod)

        for ind in range(len_arr):
            prod = prefix_prod_arr[ind] * suffix_prod_arr[len_arr-ind-1]
            prod_arr.append(prod)


        return prod_arr


        