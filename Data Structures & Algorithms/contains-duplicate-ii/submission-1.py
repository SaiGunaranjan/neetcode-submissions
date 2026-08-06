class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #if k == 0:
        #    return True

        dup_dict = {}
        for ind,val in enumerate(nums):
            if val not in dup_dict:
                dup_dict[val] = ind
            else:
                if abs(dup_dict[val] - ind) <= k:
                    return True
                else:
                    dup_dict[val] = ind
        return False


        
            
