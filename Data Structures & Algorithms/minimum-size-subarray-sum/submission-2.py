class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        lp = 0
        rp = 0
        sum_arr = nums[0]
        min_subarr_len = 100000
        while lp < n and rp < n:
            if sum_arr >= target: # valid window
                if lp == rp:
                    return 1
                min_subarr_len = min(min_subarr_len,rp-lp+1)
                sum_arr -= nums[lp]
                lp += 1
            else:
                rp += 1
                if rp > n-1:
                    break
                sum_arr += nums[rp]

        if rp-lp >= n:
            return 0
        
        return min_subarr_len


