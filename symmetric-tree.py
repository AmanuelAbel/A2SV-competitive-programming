# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)
        else:
            return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left,root.right)