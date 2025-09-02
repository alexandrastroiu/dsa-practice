# Problem: 485. Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/


# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = current_max_ones = 0
        for current_element in nums:
            current_max_ones += current_element
            max_ones = max(max_ones, current_max_ones)
            if current_element == 0:
                current_max_ones = 0

        return max_ones
