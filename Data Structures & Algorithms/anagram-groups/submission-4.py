class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            w = tuple(sorted(word))
            groups[w].append(word)
        
        result = []
        for value in groups.values():
            result.append(value)


        return result 

        