class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        iset = set(nums)
        ilist = list(iset)
        ilist.sort()
        nums.sort()
        if ilist == nums:
            return False
        else:
            return True