class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for wyk in nums[:-1]:
            while wyk in nums[nums.index(wyk)+1:]:
                nums.remove(wyk)
        return len(nums)


        