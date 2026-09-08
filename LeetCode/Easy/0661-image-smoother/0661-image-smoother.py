class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total = 0
                count = 0
                for k in range(i-1, i+2):
                    if k >= rows or k < 0:
                        continue
                    for l in range(j-1, j+2):
                        if l >= cols or l < 0:
                            continue
                        total += img[k][l]
                        count += 1
                
                ans[i][j] = total // count
        
        return ans