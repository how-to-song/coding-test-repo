class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        mem = [1, 2]

        for i in range(n-2):
            mem.append(mem[i] + mem[i+1])

        return mem[n-1]