# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indecies = {val : indx for indx, val in enumerate(inorder)}
        self.pre_indx = 0

        def dfs(l, r):
            if l > r:
                return None
                
            val = preorder[self.pre_indx]
            root = TreeNode(val)
            self.pre_indx += 1

            mid = indecies[val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(preorder)-1)