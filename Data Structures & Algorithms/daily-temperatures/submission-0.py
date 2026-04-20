class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i, tempc in enumerate(temperatures):
            found = False
            for j, temp in enumerate(temperatures[i+1:]):
                if temp > tempc:
                    result.append(j+1)
                    found = True
                    break
            if not found:    
                result.append(0)

        return result 