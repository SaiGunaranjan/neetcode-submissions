# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        list1 = []
        list2 = []
        def preorder(node,list_):

            if node is None:
                list_.append(None)
                return

            list_.append(node.val)
            preorder(node.left,list_)
            preorder(node.right,list_)

        
        preorder(p,list1)
        preorder(q,list2)

        return list1 == list2
        