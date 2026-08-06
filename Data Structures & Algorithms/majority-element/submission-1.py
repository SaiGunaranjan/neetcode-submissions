class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        len_array = len(nums)
        if len_array == 1:
            return nums[0]

        req_rep = len_array//2
        dict = {}
        for val in nums:
            if val in dict:
                dict[val] += 1
                if dict[val] > req_rep:
                     return val
            else:
                dict[val] = 1

