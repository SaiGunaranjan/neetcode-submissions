class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        for ind,val in enumerate(nums):
            if val not in dict:
                dict[target-val] = ind
            else:
                return [dict[val], ind]
        