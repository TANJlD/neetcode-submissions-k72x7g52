class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        freq = []
        for n, f in map.items():
            freq.append([f, n])

        freq = sorted(freq, reverse=True)

        return [f[1] for f in freq[:k]]

        