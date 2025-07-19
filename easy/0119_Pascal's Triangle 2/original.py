class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ly = []
        for i in range(rowIndex + 1):
            ly.append([])
            for j in range(i+1):
                ly[i].append(0)
        for k in range(rowIndex + 1):
            for w in range(len(ly[k])):
                if w == 0 or w == len(ly[k]) - 1:
                    ly[k][w] = 1
                else:
                    ly[k][w] = ly[k-1][w-1] + ly[k-1][w]
        return ly[rowIndex]
