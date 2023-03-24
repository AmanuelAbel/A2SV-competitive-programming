# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    k = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root,k,target):
            if not root:
                return
            if not root.left and not root.right:
                print(k+root.val)
                if k+root.val == target:
                    return True
            left = traverse(root.left,k+root.val,target)
            right = traverse(root.right,k+root.val,target)
            return left or right
        return traverse(root,0,targetSum)