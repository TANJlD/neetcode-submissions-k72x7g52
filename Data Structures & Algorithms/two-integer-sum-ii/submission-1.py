class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)-1):
            r = i + 1
            l = len(numbers) - 1

            wanted = target - numbers[i]

            while r <= l:
                m = (r + l) // 2
            
                if wanted == numbers[m]:
                    return [i+1, m+1]
                elif wanted > numbers[m]:
                    r = m + 1
                elif wanted < numbers[m]:
                    l = m - 1
        

        