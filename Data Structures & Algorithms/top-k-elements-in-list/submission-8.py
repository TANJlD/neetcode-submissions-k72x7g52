class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = []

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for v in dic.values():
            freq.append(v)
        freq = sorted(freq, reverse=True)

        print(freq)

        res = []

        for i in freq[:k]:
            for k, v in dic.items():
                if i == v:
                    res.append(k)
                    del dic[k]
                    break
        return res
