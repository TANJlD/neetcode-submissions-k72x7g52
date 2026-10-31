class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        subset = []

        def dfs(cur_sum, i):
            if cur_sum >= target or i >= len(candidates):
                if cur_sum == target:
                    result.append(subset.copy())
                return

            subset.append(candidates[i])
            dfs(cur_sum + candidates[i], i + 1)
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1

            subset.pop()
            dfs(cur_sum, i + 1)

        dfs(0, 0)
        return result