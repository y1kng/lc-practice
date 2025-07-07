class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        wyk = 0
        ly = len(nums) - 1

        while wyk <= ly:
            mid = (wyk + ly) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                wyk = mid + 1
            else:
                ly = mid - 1
        return wyk
