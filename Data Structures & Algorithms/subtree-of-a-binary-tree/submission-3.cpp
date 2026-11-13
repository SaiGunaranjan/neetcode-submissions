// Coded on 13/11/2026
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
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {

        if (root == nullptr and subRoot != nullptr) return false;

        if (isSameTree(root, subRoot) == false)
        {
            return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
        }
        else
            return true;
        
    }

public:
    bool isSameTree(TreeNode* p, TreeNode* q) {

        if ((p == nullptr) && (q == nullptr))
        {
            return true;
        }
        if ((p != nullptr) && (q == nullptr))
        {
            return false;
        }
        if ((p == nullptr) && (q != nullptr))
        {
            return false;
        }
        if ((p != nullptr) && (q != nullptr))
        {
            if (p->val != q->val)
            {
                return false;
            }
            else
            {
                return isSameTree(p->left, q->left) && isSameTree(p->right, q-> right);
            }
        }
    }

};
