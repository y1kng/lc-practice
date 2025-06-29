class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = len(s) - 1
        for j in range(len(s)):
            if s[j] != s[i]:
                s[j], s[i] = s[i], s[j]
                i -= 1
                if i < len(s) // 2:
                    break
            else:
                i -= 1
                if i < len(s) // 2:
                    break         
