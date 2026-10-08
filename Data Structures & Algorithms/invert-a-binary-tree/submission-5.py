# COded on 08/10/2026
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = []
        root_ = root
        
        while root_ is not None or len(stack)!=0:

            if root_ is not None:
                temp = root_.left
                root_.left = root_.right
                root_.right = temp
                stack.append(root_.right)
                root_ = root_.left
            else:
                root_ = stack.pop()
        
        return root
            

        