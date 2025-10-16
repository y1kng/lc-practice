class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0
        n = len(chars)

        while i < n:
            j = i
            chars[k] = chars[i]
            while j < n and chars[i] == chars[j]:
                j += 1
            count = j - i
            if count >= 2:
                k += 1
                for d in str(count):
                    chars[k] = d
                    k += 1
            else:
                k += 1
            i = j
        return k
