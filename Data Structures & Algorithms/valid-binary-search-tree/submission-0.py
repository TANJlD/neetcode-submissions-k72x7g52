# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        order = [float("-inf")]
        def travel(node):
            if not node:
                return True
            valid = travel(node.left)
            if node.val <= order[-1] or not valid:
                return False
            order.append(node.val)
            return travel(node.right)

        return travel(root)
        