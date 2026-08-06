class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_sets = set(nums)
        max_length = 0
        for val in num_sets:
            if val-1 not in num_sets: # Stsrt of sequence
                length = 0
                while val + length in num_sets:
                     length += 1
                max_length = max(length,max_length)

        return max_length