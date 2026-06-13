class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        ans = []

        l = 0
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1

        return ans 
                
