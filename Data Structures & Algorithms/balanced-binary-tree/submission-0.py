# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node):

            if node is None:
                return 0
            
            mhl = dfs(node.left)
            mhr = dfs(node.right)

            if abs(mhl-mhr) < 2:
                return 1 + max(mhl,mhr)
            else:
                return 10000
        

        if dfs(root) >= 10000:
            return False
        else:
            return True