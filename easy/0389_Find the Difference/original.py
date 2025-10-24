class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash1 = {}
        hash2 = {}
        for k, v in enumerate(sorted(s)):
            hash1[k] = v
        for k2, v2 in enumerate(sorted(t)):
            hash2[k2] = v2
        check = 0
        for i, j in list(hash2.items())[:-1]:
            if j != hash1[i]:
                check = 1
                break
        if check == 0:
            return list(hash2.values())[-1]
        for t, u in hash2.items():
            if u != hash1[t]:
                return u
                