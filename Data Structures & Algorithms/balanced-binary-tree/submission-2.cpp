/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {

private:
    int dfs(TreeNode *node){
            if (node == nullptr)
            {
                return 0;
            }

            int mhl = dfs(node->left);
            int mhr = dfs(node->right);

            if (abs(mhl-mhr) < 2)
            {
                return 1+max(mhl,mhr);
            }
            else
            {
                return 10000;
            }
        }


public:
    bool isBalanced(TreeNode* root) {

        

        if (dfs(root) >= 10000)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
};
