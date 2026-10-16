# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.n = 0

        def travel(node):
            if not node: return None

            ans = travel(node.left)
            if ans:
                return ans
                
            self.n += 1
            if self.n == k:
                return node 

            return travel(node.right) # if ans not in left child, it must be in right child
    
        return travel(root).val
        