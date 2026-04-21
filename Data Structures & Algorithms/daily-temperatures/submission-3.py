class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Stores [temperature, index]
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                pop_temp, pop_index = stack.pop()
                result[pop_index] = i - pop_index
            
            stack.append([temp, i])

        
        return result