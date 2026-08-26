class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        l = 0
        for r in range(len(nums)):
            while q and q[-1] < nums[r]:
                q.pop()

            q.append(nums[r])

            if r >= k:
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
                
            if q and r >= k-1:
                ans.append(q[0])

        return ans