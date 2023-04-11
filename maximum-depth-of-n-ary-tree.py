"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [[root,1]]
        res = 0
        while stack:
            node , depth = stack.pop()
            if node:
               for i in node.children:
                    stack.append([i,depth+1])
                    res = max(res,depth)
        return res+1