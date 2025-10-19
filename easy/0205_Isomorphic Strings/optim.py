class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for i, j in zip(s, t):
            if hash1.get(i, j) != j or hash2.get(j, i) != i:
                return False
            hash1[i] = j
            hash2[j] = i
        return True
        