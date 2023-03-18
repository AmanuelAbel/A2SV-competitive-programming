# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def maxdepth(root):
            if not root:
                return 0
            left = maxdepth(root.left)
            right = maxdepth(root.right)
            lleft = rright = 0
            if root.left and root.val == root.left.val:
                lleft = left + 1
            if root.right and root.val == root.right.val:
                rright = right + 1
            self.res = max(lleft + rright,self.res)
            return max(lleft,rright)
        maxdepth(root)
        return self.res