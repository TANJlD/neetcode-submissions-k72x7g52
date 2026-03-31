class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        result = []

        for num in nums:
            dic[num] += 1

        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

        for num in dic.keys():
            result.append(num)
            k = k-1
            if k == 0:
                break

        return result