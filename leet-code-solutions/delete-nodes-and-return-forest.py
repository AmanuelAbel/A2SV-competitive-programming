# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        delete = set(to_delete)
        def dfs(root):
            if not root:
                return 
            if root.val in delete:
                if root.right and root.right.val not in delete:
                    ans.append(root.right)
                if root.left and root.left.val not in delete:
                    ans.append(root.left)
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val in delete:
                root = None
            return root
        dfs(root)
        if root.val not in delete:
            ans.append(root)
        return ans
            
            