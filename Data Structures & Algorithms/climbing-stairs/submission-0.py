class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        n1 = self.climbStairs(n-1)
        n2 = self.climbStairs(n-2)

        return n1 + n2

        