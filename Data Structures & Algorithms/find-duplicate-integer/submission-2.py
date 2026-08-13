class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        sp = fp = 0
        sp = nums[sp]
        fp = nums[nums[fp]]

        while sp != fp:
            sp = nums[sp]
            fp = nums[nums[fp]]
        
        sp1 = 0
        sp2 = fp

        while sp1 != sp2:
            sp1 = nums[sp1]
            sp2 = nums[sp2]
        
        return sp1
        