from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom, mag = Counter(ransomNote), Counter(magazine)
        for c in ransom:
            if ransom[c] > mag[c]:
                return False
        return True
        