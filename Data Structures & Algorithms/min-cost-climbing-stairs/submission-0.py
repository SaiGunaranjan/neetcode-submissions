class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        def costClimb(n,cost_sum):

            if n == l - 1:
                return cost_sum
            
            cost_one_step = costClimb(n+1,cost_sum+cost[n+1])

            if n == l-2:
                return cost_sum
            else:
                cost_two_step = costClimb(n+2,cost_sum+cost[n+2])
                return min(cost_one_step,cost_two_step)

        
        l = len(cost)
        cost_sum = 0
        n = 0
        cost1 = cost_sum+cost[0]
        cost2 = cost_sum+cost[1]

        c1 = costClimb(0,cost1)
        c2 = costClimb(1,cost2)
        return min(c1,c2)

