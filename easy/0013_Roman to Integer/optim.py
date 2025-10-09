class Solution:
    def romanToInt(self, s: str) -> int:
        ly = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ik = 0
        for i in range(len(s) - 1):
            if ly[s[i]] < ly[s[i+1]]:
                ik -= ly[s[i]]
            else:
                ik += ly[s[i]]
        ik += ly[s[-1]]
        return ik
