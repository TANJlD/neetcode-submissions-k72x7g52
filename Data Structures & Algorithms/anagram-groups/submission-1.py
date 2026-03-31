class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        grouped_anagrams = []

        for str in strs:
            sorStr = tuple(sorted(str))
            if sorStr not in dic:
                dic[sorStr] = []
                dic[sorStr].append(str)
            else:
                dic[sorStr].append(str)
        
        for group in dic:
            grouped_anagrams.append(dic[group])

        return grouped_anagrams

        

        