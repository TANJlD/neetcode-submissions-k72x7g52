class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        res = []

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
    
            dic[tuple(count)].append(word)
        
        for group in dic.values():
            res.append(group)

        return res
                

    