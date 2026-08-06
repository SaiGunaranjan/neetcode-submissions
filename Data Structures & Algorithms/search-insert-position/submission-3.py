class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lp = 0
        rp = len(nums) - 1

        if target <= nums[lp]:
            return 0
        elif target == nums[rp]:
            return rp 
        elif target > nums[rp]:
            return rp + 1


        while lp <= rp:
            mid = (lp + rp) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                rp = mid - 1
            else:
                lp = mid + 1

        return rp + 1   
            