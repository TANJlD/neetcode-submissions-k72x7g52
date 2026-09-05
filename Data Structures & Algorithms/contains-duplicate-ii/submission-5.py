class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)
        l = 0
        r = 0

        while r < len(nums):
            if r > k:
                seen[nums[l]] -= 1
                l += 1

            if nums[r] in seen and seen[nums[r]] > 0:
                return True

            seen[nums[r]] += 1
            r += 1


        return False
