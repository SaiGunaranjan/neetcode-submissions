class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) == 0:
            return 0

        lp = 0
        for rp in range(len(nums)):
            if nums[rp] != val:
                nums[lp] = nums[rp]
                lp += 1

        return lp


        