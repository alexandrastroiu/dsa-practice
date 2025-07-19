# Problem: 189. Rotate Array
# Link: https://leetcode.com/problems/rotate-array/


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # solution using additional memory
        # O(n) time and O(n) space
        length = len(nums)
        k %= length
        result = [0] * length

        for i in range(length):
            result[(i + k) % length] = nums[i]

        for i in range(length):
            nums[i] = result[i]
