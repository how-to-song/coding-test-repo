class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_heap = [(score, i) for i, score in enumerate(score)]
        heapq.heapify(score_heap)
        n = len(score)
        ans = [0] * n
        
        for j in range(n-1,-1,-1):
            score, i = heapq.heappop(score_heap)
            if j < 3:
                if j == 2: ans[i] = "Bronze Medal"
                elif j == 1: ans[i] = "Silver Medal"
                elif j == 0: ans[i] = "Gold Medal"
            else:
                ans[i] = f"{j+1}"
        
        return ans