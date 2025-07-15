class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            wyk = abs(num) - 1
            if nums[wyk] > 0:
                nums[wyk] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]