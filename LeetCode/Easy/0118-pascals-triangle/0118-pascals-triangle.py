class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(numRows):
            temp = [1] * (row+1)
            if row > 0:
                for i in range(len(ans[row-1]) - 1):
                    temp[i+1] = ans[row-1][i] + ans[row-1][i+1]
            
            ans.append(temp)
        return ans