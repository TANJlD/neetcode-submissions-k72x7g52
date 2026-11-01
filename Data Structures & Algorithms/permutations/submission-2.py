class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        seen = set()

        def dfs():
            if len(curr) == len(nums):
                result.append(curr.copy())
                return

            for n in nums:
                if n not in seen:
                    curr.append(n)
                    seen.add(n)
                    dfs()
                    curr.pop()
                    seen.remove(n)
            return

        dfs()
        return result 

            