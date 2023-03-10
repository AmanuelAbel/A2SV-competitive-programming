# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        q = deque([root])
        ans = []
        res = []
        while q:
            ans.append([i.val for i in q])
            for i in range(len(q)):
                node = q.popleft()
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
        for i in ans:
            res.append(i[-1])
        return res