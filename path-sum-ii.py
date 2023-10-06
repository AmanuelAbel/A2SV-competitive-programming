# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        s = []
        ans = []
        k = 0
        def traverse(root,target,s):
            if not root:
                return
            s.append(root.val)
            if not root.left and not root.right:
                k = sum(s)
                if k == target:
                    ans.append(s[:])
            traverse(root.left,target,s)
            traverse(root.right,target,s)
            s.pop()
        traverse(root,targetSum,[])
        return ans