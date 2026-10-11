# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def travel(node):
            if not node:
                return [True, 0]

            left_balanced, left_depth = travel(node.left)
            right_balanced, right_depth = travel(node.right)
            curr_depth = 1 + max(left_depth, right_depth)

            if abs(left_depth - right_depth) > 1:
                return [False, curr_depth]
            
            if left_balanced and right_balanced:
                return [True, curr_depth]
            else:
                return [False, curr_depth]

        
        balanced, depth = travel(root)
        return balanced
        