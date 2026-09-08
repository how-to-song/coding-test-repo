class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = []
        for stone in stones:
            heapq.heappush(stones_heap, (-stone, stone))
        
        while len(stones_heap) >= 2:
            y = heapq.heappop(stones_heap)[1]
            x = heapq.heappop(stones_heap)[1]

            if x == y:
                continue

            y -= x
            heapq.heappush(stones_heap, (-y, y))
        
        if len(stones_heap) == 0:
            return 0
            
        return heapq.heappop(stones_heap)[1]

        