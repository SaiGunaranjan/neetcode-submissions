class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        lp = 0
        rp = k
        List = []
        while rp < len(nums) + 1:
            List.append(max(nums[lp:rp]))
            lp += 1
            rp += 1

        return List
