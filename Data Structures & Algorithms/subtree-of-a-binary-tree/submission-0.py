# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if self.compare(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


    def compare(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        if self.compare(p.left, q.left) and self.compare(p.right, q.right):
            return True
        else:
            return False