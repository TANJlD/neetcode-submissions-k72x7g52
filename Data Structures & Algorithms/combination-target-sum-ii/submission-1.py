class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        freq = defaultdict(int)
        for n in candidates:
            freq[n] += 1
        uniques = list(set(candidates))
        result = []
        subset = []
        count = defaultdict(int)
        size = len(uniques)

        def dfs(cur_sum, start): 
            if cur_sum >= target:
                if cur_sum == target:
                    result.append(subset.copy())
                return
                
            for i in range(start, size):
                num = uniques[i]
                subset.append(num)
                count[num] += 1

                if freq[num] > count[num]:
                    dfs(cur_sum + num, i)
                else:
                    dfs(cur_sum + num, i + 1)

                count[subset.pop()] -= 1

        dfs(0, 0)
        return result
        