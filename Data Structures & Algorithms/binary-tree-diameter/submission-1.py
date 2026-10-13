# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        
        self.max_dia = 0

        def dfs(node):

            if node is None:
                return 0
            
            maxheight_leftsubtree = dfs(node.left)
            maxheight_rightsubtree = dfs(node.right)

            self.max_dia = max(self.max_dia,maxheight_leftsubtree+maxheight_rightsubtree)

            return 1+max(maxheight_leftsubtree,maxheight_rightsubtree)

        
        _ = dfs(root)

        return self.max_dia
        