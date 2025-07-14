class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        for wyk in set(nums):
            if first is None or wyk > first:
                first, second, third = wyk, first, second
            elif second is None or wyk > second:
                second, third = wyk, second
            elif third is None or wyk > third:
                third = wyk
        return third if third is not None else first