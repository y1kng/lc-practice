class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1
        for index, value in enumerate(s):
            if count[value] == 1:
                return index
        return -1
        