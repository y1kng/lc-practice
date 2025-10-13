class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        i = 0
        res = []

        while i < n:
            j = i
            while j < n and s[i] == s[j]:
                j += 1
            if j - i >= 3:
                res.append([i, j - 1])
            i = j
        return res
