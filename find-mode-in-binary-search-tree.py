# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)
        counter = 0
        res = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            ans[root.val] += 1
            traverse(root.right)
        traverse(root)
        z = max(ans.values())
        for i in ans:
            if ans[i] == z:
                res.append(i)
        return res