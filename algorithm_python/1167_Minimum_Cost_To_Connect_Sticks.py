import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        # greedy: connect min first
        # min heap
        ans = 0
        heap = sticks
        heapq.heapify(heap)
        # repeatedly get two min sticks
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            heapq.heappush(heap, first + second)
            ans += first + second

        return ans