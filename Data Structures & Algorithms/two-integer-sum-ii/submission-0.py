class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lp = 0
        rp = len(numbers) - 1
        while lp < rp:
            if numbers[lp] + numbers[rp] < target:
                lp += 1
                continue
            if numbers[lp] + numbers[rp] > target:
                rp -=1
                continue
            else:
                return [lp+1, rp+1]