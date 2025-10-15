class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            j = i
            if s[j] != ' ':
                while j < len(s) and s[j] != ' ':
                    j += 1
                count += 1
            else:
                j += 1
            i = j
        return count
