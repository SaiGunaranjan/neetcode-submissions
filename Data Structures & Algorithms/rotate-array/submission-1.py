class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_arr = len(nums)
        new_k = k % len_arr

        lp = 0
        rp = len_arr - 1
        while lp < rp:
            nums[rp], nums[lp] = nums[lp], nums[rp]
            lp += 1
            rp -= 1
        
        lp = 0
        rp = new_k - 1
        while lp < rp:
            nums[rp], nums[lp] = nums[lp], nums[rp]
            lp += 1
            rp -= 1

        lp = new_k
        rp = len_arr - 1
        while lp < rp:
            nums[rp], nums[lp] = nums[lp], nums[rp]
            lp += 1
            rp -= 1

