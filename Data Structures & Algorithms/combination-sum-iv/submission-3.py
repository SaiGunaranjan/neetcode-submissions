class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        if target == 0:
            return 1
        if target < min(nums):
            return 0
        
        combs = [0]*(target+1)

        for i in range(1,target+1):
            count = 0
            for val in nums:
                if val <= i:
                    rem = i-val
                    if rem==0:
                        count+=1
                    else:
                        count += combs[rem]
            combs[i] = count

        return combs[-1]