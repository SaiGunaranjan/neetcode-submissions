# Coded on 28/09/2026
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        stack = []
        my_list = []

        while root is not None or len(stack)!=0:

            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                my_list.append(root.val)
                root = root.right
        
        return my_list
        