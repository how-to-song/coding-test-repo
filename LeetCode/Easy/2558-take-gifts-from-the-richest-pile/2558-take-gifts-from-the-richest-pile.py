class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts_heap = [-g for g in gifts]
        heapq.heapify(gifts_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(gifts_heap)
            heapq.heappush(gifts_heap, -math.isqrt(largest))
        
        return sum(gifts_heap) * (-1)