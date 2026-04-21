class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([temp, i])
            elif temp > stack[-1][0]:
                while stack and temp > stack[-1][0]:
                    imp = stack.pop()
                    result[imp[1]] = i - imp[1]
                stack.append([temp, i])
            else:
                stack.append([temp, i])

        while stack:
            imp = stack.pop()
            result[imp[1]] = 0

        return result

        