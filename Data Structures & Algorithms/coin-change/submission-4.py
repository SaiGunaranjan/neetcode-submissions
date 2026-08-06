class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        arr = [amount+1]*(amount + 1)
        arr[0] = 0

        for val in range(1,amount+1):
            min_coins = amount+1
            for denom in coins:
                 if (denom <= val) and (arr[val-denom] < min_coins):
                    min_coins = arr[val-denom]
            if min_coins != amount+1:
                arr[val] = min_coins + 1

        if arr[-1] != amount+1:
            return arr[-1]
        else:
            return -1



