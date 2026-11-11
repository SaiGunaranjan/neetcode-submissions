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
#include <vector>
using namespace std;

class Solution {

private:
    void preorder(TreeNode* node, vector<int>& list_)
        {
            if (node == nullptr)
            {
                list_.push_back(10000); // Placeholder for None values
                return;
            }

            list_.push_back(node->val);
            preorder(node->left, list_);
            preorder(node->right, list_);
        }

public:
    bool isSameTree(TreeNode* p, TreeNode* q) {

        vector<int> list1;
        vector<int> list2;
        
        preorder(p,list1); // Passing list1 already passes by reference
        preorder(q,list2);

        return list1 == list2;
        
    }
};
