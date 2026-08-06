class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_arr = len(nums)
        for i in range(len_arr-1):
            min_ele = nums[i]
            min_ind = i
            for j in range(i+1,len_arr):
                if nums[j] < min_ele:
                    min_ele = nums[j]
                    min_ind = j

            temp = nums[i]
            nums[i] = nums[min_ind]
            nums[min_ind] = temp
