# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None and root2 is not None:
            return root2
        if root1 is not None and root2 is None:
            root2 = root1
            return root2
        if root1 is not None and root2 is not None:
            root2.val = root1.val + root2.val
            wyk = self.mergeTrees(root1.left, root2.left)
            ly = self.mergeTrees(root1.right, root2.right)
            root2.left = wyk
            root2.right = ly
            return root2
        