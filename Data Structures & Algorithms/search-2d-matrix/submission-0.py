class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        tp = 0
        bp = len(matrix) - 1

        while (tp <= bp):
            mp = (tp + bp) // 2
            if target > matrix[mp][-1]:
                tp = mp + 1
            elif target < matrix[mp][0]:
                bp = mp - 1
            else:
                lp = 0
                rp = len(matrix[0]) - 1
                while lp <= rp:
                    mid = (lp + rp)//2
                    if target == matrix[mp][mid]:
                        return True
                    elif target > matrix[mp][mid]:
                        lp = mid + 1
                    else:
                        rp = mid - 1
                break
        return False