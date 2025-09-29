# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def like(root: Optional[TreeNode]):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [root.val]
            wyk = like(root.left)
            ly = like(root.right)
            ik = wyk + [root.val] + ly
            return ik
    
        uu = like(root)

        dummy = TreeNode(0)
        curr = dummy
        for i, k in enumerate(uu):
            curr.val = k
            if i != len(uu) - 1:
                curr.right = TreeNode(0)
                curr = curr.right
        return dummy