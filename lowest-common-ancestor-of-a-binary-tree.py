# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res =None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(current):
            if not current:
                return False
            left = traverse(current.left)
            right = traverse(current.right)
            half = current == p or current == q
            if half + left + right >= 2:
                self.res = current
            return half or left or right
        traverse(root)
        return self.res