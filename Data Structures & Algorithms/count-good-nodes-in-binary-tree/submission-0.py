# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def travel(node, max_val):
            nonlocal count
            if not node:
                return

            if node.val >= max_val:
                count += 1

            travel(node.left, max(max_val, node.val))
            travel(node.right, max(max_val, node.val))

        travel(root, root.val)
        return count
        