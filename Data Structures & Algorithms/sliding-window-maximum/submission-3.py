class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heapq = MaxHeap(nums[:k])
        heapq.maxHeap()
        ans = [max(nums[:k])]
        

        l = 0
        for r in range(k, len(nums)):
            heapq.heappush(nums[r])
            num = heapq.heappop(nums[l])
            ans.append(num)
            l += 1

        return ans




class MaxHeap:
    def __init__(self, nums):
        self.max_heap = nums

    def maxHeap(self):
        n = len(self.max_heap)
        last_non_leaf = (n // 2) - 1

        for i in range(last_non_leaf, -1, -1):
            self.heapify(n, i)

    def heapify(self, n, i):
        largest = i
        left_child = (2 * i) + 1
        right_child = (2 * i) + 2

        if left_child < n and self.max_heap[left_child] > self.max_heap[largest]:
            largest = left_child
        if right_child < n and self.max_heap[right_child] > self.max_heap[largest]:
            largest = right_child

        if largest != i:
            self.max_heap[largest], self.max_heap[i] = self.max_heap[i], self.max_heap[largest]
            self.heapify(n, largest)

    def heappush(self, val):
        self.max_heap.append(val)

        current = len(self.max_heap) - 1

        while current > 0:
            parent = (current - 1) // 2

            if self.max_heap[current] > self.max_heap[parent]:
                self.max_heap[current], self.max_heap[parent] = self.max_heap[parent], self.max_heap[current]
                current = parent
            else:
                break

    def heappop(self, val):
        for i in range(len(self.max_heap)):
            if self.max_heap[i] == val:
                break
        if i < len(self.max_heap)-1:
            self.max_heap[i] = self.max_heap.pop()
            self.heapify(len(self.max_heap), i)
        else:
            self.max_heap.pop()

        return self.max_heap[0]








