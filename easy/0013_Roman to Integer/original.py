class Solution:
    def romanToInt(self, s: str) -> int:
        ly = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        wyk = []
        i = 0
        while i < len(s):
            if (i + 1) < len(s) and ly[s[i]] >= ly[s[i+1]] or i == len(s) - 1:
                wyk.append(ly[s[i]])
                i += 1
            elif (i + 1) < len(s) and ly[s[i]] < ly[s[i+1]]:
                wyk.append(ly[s[i+1]] - ly[s[i]])
                if (i + 2) < len(s):
                    i += 2
                elif (i + 2) == len(s):
                    return sum(wyk)
        return sum(wyk)