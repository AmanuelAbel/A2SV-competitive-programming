# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = ([root])
        visited = set([root])
        res = []
        while queue:
            add = 0
            for r in queue:
                add += r.val
            res.append(add/len(queue))
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right:
                    queue.append(node.right)
                    visited.add(node.right)
        return res