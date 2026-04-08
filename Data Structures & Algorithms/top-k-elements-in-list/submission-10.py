class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        dic = {}
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for k, v in dic.items():
            freq[v].append(k)
        
        result = []
 
        for b in reversed(freq):
            if len(b) != 0:
                for n in b:
                    result.append(n)
                    if len(result) == K:
                        return result
