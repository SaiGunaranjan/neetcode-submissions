class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        freq_dict = {}
        for ind,val in enumerate(nums):
            if val not in freq_dict:
                freq_dict[val] = 1
            else:
                return val
        