# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        self.levels = []

        def travel(node, depth):
            if not node:
                return 
            if depth > len(self.levels):
                self.levels.append([])
            self.levels[depth - 1].append(node.val)
            travel(node.left, depth + 1)
            travel(node.right, depth + 1) 

        travel(root, 1)
        return self.levels
        