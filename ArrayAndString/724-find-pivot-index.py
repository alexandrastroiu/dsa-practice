# Problem: 724. Find Pivot Index
# Link: https://leetcode.com/problems/find-pivot-index/


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot_index = -1
        length = len(nums)
        sums = [0] * length
        sums[0] = nums[0]

        for i in range(1, length):
            sums[i] = sums[i - 1] + nums[i]

        for i in range(length):
            if i == 0:
                right_sum = sums[length - 1] - sums[0]
                left_sum = 0
            elif i == length - 1:
                right_sum = 0
                left_sum = sums[i - 1]
            else:
                right_sum = sums[i - 1]
                left_sum = sums[length - 1] - sums[i]
            if right_sum == left_sum:
                pivot_index = i
                break

        return pivot_index
