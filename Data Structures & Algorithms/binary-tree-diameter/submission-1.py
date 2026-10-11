# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter

            if not node:
                return 0
            
            max_depth_left = dfs(node.left)
            max_depth_right = dfs(node.right)
            curr_diameter = max_depth_left + max_depth_right
            max_diameter = max(max_diameter, curr_diameter)

            return 1 + max(max_depth_left, max_depth_right)

        dfs(root)
        return max_diameter