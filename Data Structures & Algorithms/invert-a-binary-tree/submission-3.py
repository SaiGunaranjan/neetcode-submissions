# Coded on 08/10/2026
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swap_left_right(node):

            if node is None:
                return
            else:
                temp = node.left
                node.left = node.right
                node.right = temp
            # Pre-order traversal --> root(done outside the recursion function), left, right
            swap_left_right(node.left)
            swap_left_right(node.right)
        
        swap_left_right(root) # Swap root node

        return root