class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []

        for i in range(len(nums1)-1, -1, -1):
            
            while nums2 and nums2[-1] > nums1[i]:
                merged.append(nums2.pop())
                
            merged.append(nums1[i])

        while nums2:
            merged.append(nums2.pop())

        length = len(merged)
        m = length // 2

        if length % 2:
            return merged[m]
        else:
            return ((merged[m] + merged[m-1]) / 2)
            return merged[m]