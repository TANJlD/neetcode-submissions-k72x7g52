# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        self.levels = defaultdict(list)

        def travel(node, depth):
            if not node:
                return 0
            self.levels[depth].append(node.val) 
            return 1 + max(travel(node.left, depth + 1), travel(node.right, depth + 1))

        ans = []
        max_depth = travel(root, 1)
        for i in range(max_depth):
            ans.append(self.levels[i+1])

        return ans
        