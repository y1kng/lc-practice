class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        wyk = set(nums)
        if len(wyk) < 3:
            return max(wyk)
        ly = sorted(wyk)
        ik = list(reversed(ly))
        return ik[2]