class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        wyk = []
        for i in range(numRows):    
            row = []       
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(wyk[i-1][j-1] + wyk[i-1][j])
            wyk.append(row)
        return wyk
                    