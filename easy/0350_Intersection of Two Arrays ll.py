class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ly = []
        for wyk in nums1:
            if wyk in nums2:
                ly.append(wyk)
                nums2.remove(wyk)
        return ly
        