# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root
        else:
            q = [root]

        while len(q)!=0:
            root_ = q.pop(0)
            temp = root_.left
            root_.left = root_.right
            root_.right = temp
            if root_.left is not None:
                q.append(root_.left)
            if root_.right is not None:
                q.append(root_.right)

        return root
        