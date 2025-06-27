from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        wyk = Counter(nums)
        for i, j in wyk.items():
            if j == 1:
                return i
