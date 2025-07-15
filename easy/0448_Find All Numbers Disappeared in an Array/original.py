class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        wyk = set()
        for i in range(1, len(nums)+1):
            wyk.add(i)
        ly = set(nums)
        return list(wyk - ly)
