# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is not None and root.right is None:
            targetSum -= root.val
            wyk = self.hasPathSum(root.left, targetSum)
            return wyk
        if root.right is not None and root.left is None:
            targetSum -= root.val
            wyk = self.hasPathSum(root.right, targetSum)
            return wyk
        if root.left is not None and root.right is not None:
            targetSum -= root.val
            wyk = self.hasPathSum(root.left, targetSum)
            ly = self.hasPathSum(root.right, targetSum)
            if wyk == True or ly == True:
                return True
            else:
                return False
        if root.left is None and root.right is None:
            if targetSum - root.val == 0:
                return True
            else:
                return False
           