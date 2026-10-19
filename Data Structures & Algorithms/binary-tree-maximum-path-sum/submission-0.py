class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.max_val = float("-inf")

        def dfs(root):
            if not root:
                return float("-inf")

            sum_of_left = dfs(root.left)
            sum_of_right = dfs(root.right)

            total_sum = root.val + sum_of_left + sum_of_right    

            self.max_val = max(
                self.max_val,
                root.val, 
                sum_of_left + root.val,
                sum_of_right + root.val, 
                total_sum
            )

            return max(root.val, sum_of_left + root.val, sum_of_right + root.val)
        
        dfs(root)
        return self.max_val