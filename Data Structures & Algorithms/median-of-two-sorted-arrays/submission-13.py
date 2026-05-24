class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A) - 1
        while True:
            m1 = (l+r) // 2
            m2 = half - m1 - 2

            A_left = A[m1] if m1 >= 0 else float("-infinity")
            A_right = A[m1+1] if (m1+1) <= len(A)-1 else float("infinity")
            B_left = B[m2] if m2 >= 0 else float("-infinity")
            B_right = B[m2+1] if (m2+1) <= len(B)-1 else float("infinity")


            if A_left <= B_right and A_right >= B_left:
                if total % 2:
                    return min(A_right, B_right)
                else:
                    a = max(A_left, B_left)
                    b = min(A_right, B_right)
                    return (a+b) / 2
            elif A_left > B_right:
                r = m1 - 1
            else:
                l = m1 + 1