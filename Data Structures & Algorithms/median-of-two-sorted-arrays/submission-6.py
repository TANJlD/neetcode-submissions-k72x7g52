class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A = nums1
            B =  nums2
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

            if m1 < 0:
                r_of_lpar = B[m2] 
            elif m2 < 0: 
                r_of_lpar = A[m1] 
            else: 
                r_of_lpar = max(A[m1], B[m2])
                
            l_of_rpar = min(A[m1+1], B[m2+1]) if (m1+1) <= (len(A)-1) else B[m2+1]

            if r_of_lpar > l_of_rpar:
                if A[m1] < B[m1]:
                    l = m1+1
                else:
                    r = m1-1
            else:
                if total % 2:
                    return l_of_rpar
                return (r_of_lpar + l_of_rpar) / 2
         