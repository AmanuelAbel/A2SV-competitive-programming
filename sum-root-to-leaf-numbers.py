# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []        
        def traverse(root,s):
            if not root:
                return
            if not root.left and not root.right:
                ans.append(s+str(root.val))
            traverse(root.left,s+str(root.val))
            traverse(root.right,s+str(root.val))
        traverse(root,"")
        counter = sum(map(int,ans))
        return counter