class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                if nums[m] < nums[r]: # r side is sorted
                    r = m - 1
                else: # if r side not sorted, l side must be sorted
                    if nums[l] > target: # if target not in left side, discard l side 
                        l = m + 1
                    else: 
                        r = m - 1
            
            elif nums[m] < target:
                if nums[m] > nums[l]: # l side is sorted 
                    l = m + 1
                else: # if l side not sorted, r side must be sorted
                    if nums[r] < target: # if target not in r side, discard r side
                        r = m - 1
                    else:
                        l = m + 1


            else:
                return m

        return -1 