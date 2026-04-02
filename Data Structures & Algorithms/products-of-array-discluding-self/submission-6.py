class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i, num in enumerate(nums[:-1]):
            if i == 0:
                result.append(num)
            else:
                result.append(num * result[i-1])

        result = [1] + result
        # return result
        l = len(nums)

        for i, num in enumerate(reversed(nums[1:])):
            if i == 0:
                r = num
            else:
                r = r * num

            result[l-2 - i] = result[l-2 - i] * r

        return result


        