# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        d = defaultdict(int)
        d[0] += 1
        def traverse(root,sums):
            nonlocal ans
            if not root:
                return 

            sums += root.val

            ans += d[sums - targetSum]

            d[sums] += 1
            
            traverse(root.left, sums )
            traverse(root.right, sums )
            d[sums] -= 1
            
        traverse(root,0)
        return ans