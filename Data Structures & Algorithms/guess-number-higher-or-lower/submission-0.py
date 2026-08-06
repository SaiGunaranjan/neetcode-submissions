# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        lp = 1
        rp = n
        while lp <= rp:
            mid = (lp + rp)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                rp = mid - 1
            else:
                lp = mid + 1


        