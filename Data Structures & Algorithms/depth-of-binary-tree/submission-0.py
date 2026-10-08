# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(root,count):

            if root is None:
                return count-1
            
            count_left = depth(root.left,count+1)
            count_right = depth(root.right,count+1)

            return max(count_left,count_right)
        
        return depth(root,1)