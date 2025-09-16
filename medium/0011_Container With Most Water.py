# Title: Container With Most Water (11) - Two Pointer Approach

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        space = 0
        j = len(height) - 1
        while i < j:
            if (min(height[i], height[j])) * (j-i) > space:
                space = (min(height[i], height[j])) * (j-i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return space

"""
Explanation / My Thought Process:

- Problem: Given an array of heights, find two lines forming a container with the maximum area.

- Key Idea: The area is determined by the shorter line. Only moving the pointer of the shorter line can potentially yield a bigger area.

- Approach: Use two pointers, i at the start and j at the end, and a variable 'space' to keep track of max area.

- Loop: while i < j, calculate area, update space, move the smaller pointer.

- Example: height = [1,8,6,2,5,4,8,3,7], start with 1*7, then move the left pointer, continue checking...

- Time Complexity: O(n), each pointer moves at most n steps.

- Space Complexity: O(1), only a few variables used.

"""