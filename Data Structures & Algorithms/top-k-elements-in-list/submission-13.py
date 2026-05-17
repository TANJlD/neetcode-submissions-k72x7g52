class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for _ in range(len(nums)+1)]
        print(freq)

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        print(map)

        for n, f in map.items():
            freq[f].append(n)
        print(freq)
        ans = []
        for i in range(len(freq)-1, 0, -1):
            while freq[i]:
                ans.append(freq[i].pop())
                if len(ans) == k:
                    return ans   