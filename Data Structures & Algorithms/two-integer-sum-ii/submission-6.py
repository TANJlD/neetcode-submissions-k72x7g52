class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        for i, num1 in enumerate(numbers):
            num2 = target - num1
            l = i
            r = n
            while l <= r:
                m = (l+r) // 2
                if numbers[m] < num2:
                    l = m + 1
                elif numbers[m] > num2:
                    r = m - 1
                else:
                    return [i+1, m+1]