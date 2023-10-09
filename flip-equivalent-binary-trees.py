# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2):
            return False
        if root1.val != root2.val:
            return False
        queue1 = []
        queue2 = []
        queue1.append(root1)
        queue2.append(root2)
        set1 = set()
        set1.add(root1.val)
        set2 = set()
        set2.add(root2.val)
        
        while queue1 and queue2:
            if len(queue1) != len(queue2):
                return False
            
            
            for i in range(len(queue1)):
                node1 = queue1.pop(0)
                set1.remove(node1.val)
                for index,i in enumerate(queue2):
                    if i.val == node1.val:
                        node2 = i
                        queue2.pop(index)
                        set2.remove(node2.val)
                        break
                if node1 and node1.left:
                    queue1.append(node1.left)
                    set1.add(node1.left.val)
                if node1 and node1.right:
                    queue1.append(node1.right)
                    set1.add(node1.right.val)
                if node2 and node2.left:
                    queue2.append(node2.left)
                    set2.add(node2.left.val)
                if node2 and node2.right:
                    queue2.append(node2.right)
                    set2.add(node2.right.val)
                if set1 != set2:
                    print(set1,set2)
                    return False
        return True