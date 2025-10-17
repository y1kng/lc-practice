class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        chunk1 = 0
        count = 0
        for j in range(len(s)):
            if s[i] != s[j]:
                chunk2 = j - i
                count += min(chunk1, chunk2)
                chunk1 = chunk2
                i = j
        n = min(chunk1, (j + 1) - i) 
        
        return count + n
        