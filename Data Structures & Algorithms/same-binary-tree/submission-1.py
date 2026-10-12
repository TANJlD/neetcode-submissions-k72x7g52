# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
            
        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1.val != node2.val:
                return False

            if node1.left: stack1.append(node1.left)
            if node2.left: stack2.append(node2.left)

            if len(stack1) != len(stack2):
                return False

            if node1.right: stack1.append(node1.right)
            if node2.right: stack2.append(node2.right)

            if len(stack1) != len(stack2):
                return False

        return len(stack1) == len(stack2)