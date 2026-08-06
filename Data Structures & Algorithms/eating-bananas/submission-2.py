class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        total_bananas = sum(piles)
        lp = math.ceil(total_bananas/h)
        rp = total_bananas
        min_eating_rate = 1000000000000
        while lp <= rp:
            mp = (lp + rp)//2 
            count = 0
            for val in piles:
                count += math.ceil(val/mp)
            if count <= h:
                min_eating_rate = min(min_eating_rate,mp)
                rp = mp-1
            else:
                lp = mp+1

        return min_eating_rate
        