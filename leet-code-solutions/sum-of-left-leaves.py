# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 
            if not root.left and not root.right:
                res += root.val
            dfs(root.left)
            if root.right and (root.right.left or root.right.right):
                dfs(root.right)
        dfs(root)
        if root and not root.left and not root.right:
            res -= root.val
        return res