class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash1 = {}
        hash2 = {}
        for i in ransomNote:
            hash1[i] = hash1.get(i, 0) + 1
        for j in magazine:
            hash2[j] = hash2.get(j, 0) + 1
        for k, v in hash1.items():
            if (k not in hash2) or (hash1[k] > hash2[k]):
                return False
        return True
