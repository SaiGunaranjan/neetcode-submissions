class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cumsum_dict = {}
        cumsum_dict[0] = 1
        cumsum = 0 # Init
        total_num_subarrays = 0
        for val in nums:
            cumsum += val
            if cumsum - k in cumsum_dict:
                total_num_subarrays += cumsum_dict[cumsum - k]
            if cumsum in cumsum_dict:
                cumsum_dict[cumsum] += 1
            else:
                cumsum_dict[cumsum] = 1
            
        
        return total_num_subarrays

