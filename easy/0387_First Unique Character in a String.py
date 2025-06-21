class Solution:
    def firstUniqChar(self, s: str) -> int:
        for wyk in s:
            if wyk not in s[s.index(wyk)+1:]:
                return s.index(wyk)
        return -1
                

        