class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        lp = max(weights)
        rp = sum(weights)
        min_weight_capacity = 25000000
        while lp <= rp:

            mp = (lp+rp)//2
            cumsum = 0
            count = 0
            for i in range(len(weights)):

                if cumsum + weights[i] <= mp:
                    cumsum += weights[i]
                else:
                    count += 1
                    cumsum = weights[i]
            count += 1
            if count <= days:
                rp = mp - 1
                min_weight_capacity = min(min_weight_capacity,mp)
            elif count > days:
                lp = mp + 1

        return min_weight_capacity