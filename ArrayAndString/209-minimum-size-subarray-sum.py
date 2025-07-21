# Problem: 209. Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # using the Sliding Window technique
        left = right = current_sum = 0
        length = len(nums)
        minimal_length = float("inf")

        for right in range(length):
            current_sum += nums[right]

            while current_sum >= target:
                minimal_length = min(minimal_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return minimal_length if minimal_length != float("inf") else 0
