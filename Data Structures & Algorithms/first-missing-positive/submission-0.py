class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        hash_set = set(nums)

        min_val = 1
        for i in range(len(hash_set)):
            if min_val in hash_set:
                min_val += 1

        return min_val

