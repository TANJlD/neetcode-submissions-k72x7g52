class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = []
        right = []
        for i, num in enumerate(nums):
            if i == 0:
                left.append(num)
            else:
                left.append(num + left[i-1])

        for i, num in enumerate(reversed(nums)):
            if i == 0:
                right.append(num)
            else:
                right.append(num + right[i-1])
        
        right.reverse()

        for i in range(len(nums)):
            if right[i] == left[i]:
                return i
                
        return -1

        