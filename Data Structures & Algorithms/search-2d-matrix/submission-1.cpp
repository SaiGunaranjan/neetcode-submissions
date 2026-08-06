class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int nrows = matrix.size();
        int ncols = matrix[0].size();
        int tp = 0;
        int bp =  nrows - 1;

        while (tp <= bp)
        {
            int mp = floor((tp + bp) / 2);
            if (target > matrix[mp][ncols-1])
            {
                tp = mp + 1;
            }
            else if (target < matrix[mp][0])
            {
                bp = mp - 1;
            }
            else
            {
                int lp = 0;
                int rp = ncols - 1;
                while (lp <= rp)
                {
                    int mid = floor((lp + rp)/2);
                    if (target == matrix[mp][mid])
                    {
                        return true;
                    }
                        
                    else if (target > matrix[mp][mid])
                    {
                        lp = mid + 1;
                    }
                    else
                    {
                        rp = mid - 1;
                    }
                        
                }
                break;
            }
        }
            
        return false;
        
    }
};
