# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        min_left = self.minDepth(root.left)
        min_right = self.minDepth(root.right)

        if min_left == 0 or min_right == 0:
            return max(min_left, min_right) + 1

        return min(min_left, min_right) + 1 