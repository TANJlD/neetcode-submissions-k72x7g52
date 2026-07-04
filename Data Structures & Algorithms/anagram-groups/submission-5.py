class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            count = tuple(count)
            anagrams[count].append(word)

        result = []

        for sub in anagrams.values():
            result.append(sub)

        return result 
