class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        lp = 0
        for rp in range(1,len(nums)):
            if nums[rp] == nums[lp]:
                rp +=1
            else:
                lp += 1
                nums[lp] = nums[rp]
                rp+=1
        
        return lp + 1
        