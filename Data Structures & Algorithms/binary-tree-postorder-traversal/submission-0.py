# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        my_list = []
        if root is None:
            return my_list
        
        def postorder(root):

            if root is None:
                return
            
            postorder(root.left)
            postorder(root.right)
            my_list.append(root.val)
            
            return my_list

        my_list = postorder(root)
        return my_list
        