# Coded on 20/09/2026
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        my_list = []
        if root is None:
            return my_list

        def preorder(root):

            if root is None:
                return
            
            my_list.append(root.val)
            preorder(root.left)
            preorder(root.right)

            return my_list


        my_list = preorder(root)
        return my_list
        