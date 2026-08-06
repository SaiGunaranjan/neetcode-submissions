class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        len_arr = len(nums)
        num_repeats = len_arr // 3
        #import numpy as np
        #vals,counts = np.unique(np.array(nums),return_counts=True)
        

        #return list(vals[counts > num_repeats])

        dict_counts = {}
        valid_list = []
        for val in nums:
            if val in dict_counts:
                dict_counts[val] += 1
            else:
                dict_counts[val] = 1
            if (dict_counts[val] > num_repeats) and (val not in valid_list):
                    valid_list.append(val)

        return valid_list

        