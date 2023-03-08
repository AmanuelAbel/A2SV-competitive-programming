# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []
        s = ""
        def validate(root,s,arr):
            if root:
                s+=str(root.val)+"->"
                if not root.left and not root.right:
                    arr.append(s[:-2])
                validate(root.left,s,arr)
                validate(root.right,s,arr)
            
        validate(root,s,arr)

        return arr