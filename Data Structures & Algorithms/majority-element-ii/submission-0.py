class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        import numpy as np

        len_arr = len(nums)
        vals,counts = np.unique(np.array(nums),return_counts=True)
        num_repeats = len_arr // 3

        return list(vals[counts > num_repeats])
        