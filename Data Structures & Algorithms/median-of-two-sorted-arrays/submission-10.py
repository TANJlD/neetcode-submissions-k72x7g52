class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            B = nums1
            A = nums2

        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A) - 1

        while True:
            m1 = (l+r) // 2
            m2 = half - m1 - 2

            Aleft = A[m1] if m1 >= 0 else float("-infinity")
            Aright = A[m1+1] if (m1+1) <= (len(A)-1) else float("infinity")
            Bleft = B[m2] if m2 >= 0 else float("-infinity")
            Bright = B[m2+1] if (m2+1) <= (len(B)-1) else float("infinity")

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    a = max(Aleft, Bleft)
                    b = min(Aright, Bright)
                    return (a+b) / 2
            elif Aleft > Bright:
                r = m1 - 1
            elif Bleft > Aright:
                l = m1 + 1



        