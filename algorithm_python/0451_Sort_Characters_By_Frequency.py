from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        
        # hash map
        counter = Counter(s)
        # max heap
        heap = []
        for char in s:
            heapq.heappush(heap, (-counter[char], char))
        ans = []
        while heap:
            freq, char = heapq.heappop(heap)
            ans.append(char)

        return ''.join(ans)