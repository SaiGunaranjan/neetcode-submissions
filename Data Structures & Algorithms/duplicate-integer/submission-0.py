class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        import numpy as np

        uniq_ele = np.unique(np.array(nums))
        if len(uniq_ele) == len(nums):
            return False
        else:
            return True
            
        