# Problem: 747. Largest Number At Least Twice of Others
# Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = -1
        max_index = 0
        length = len(nums)

        for i in range(length):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                max_index = i
            elif nums[i] > max2:
                max2 = nums[i]

        if max1 >= (2 * max2):
            return max_index
        else:
            return -1
