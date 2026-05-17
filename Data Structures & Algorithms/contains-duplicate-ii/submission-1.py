class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}

        for i in range(len(nums)):
            if nums[i] not in dup:
                dup[nums[i]] = i
            else:
                if abs(dup[nums[i]]-i) <= k:
                    return True 
                else:
                    dup[nums[i]] = i
        print(dup)
        return False
        