# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        counter = 0
        ans = []
        def traverse(root):
            if not root:
                return
            ans.append(root.val)
            traverse(root.left)
            traverse(root.right)
        def check(root):
            nonlocal counter
            if not root:
                return 
            traverse(root)
            add = 0
            for i in range(len(ans)):
                add += ans[i]
            if add // (len(ans)) ==  root.val:
                counter += 1
            ans.clear()
            check(root.left)
            check(root.right)
            return counter
        check(root)
        return counter