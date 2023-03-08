# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if p and not q:
                return False
            if not p and q:
                return False
            if p.val == q.val:
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
            else:
                return False
        def finds(root,subRoot):
            z = False
            if not root or not subRoot:
                return
            if root.val == subRoot.val:
                z = isSameTree(root,subRoot)
            left = finds(root.left,subRoot)
            right = finds(root.right,subRoot)
            return z or left or right

        return finds(root,subRoot)