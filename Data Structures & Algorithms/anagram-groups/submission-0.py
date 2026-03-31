class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        grouped_anagrams = []

        for str in strs:
            if tuple(sorted(str)) not in dic:
                dic[tuple(sorted(str))] = []
                dic[tuple(sorted(str))].append(str)
            else:
                dic[tuple(sorted(str))].append(str)
        
        for group in dic:
            grouped_anagrams.append(dic[group])

        return grouped_anagrams

        

        