# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        my_list = []

        while root is not None or len(stack)!=0:

            if root is not None:
                my_list.append(root.val)
                stack.append(root.left)
                root = root.right
            else:
                root = stack.pop()
        
        return my_list[::-1]
        