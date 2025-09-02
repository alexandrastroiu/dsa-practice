# Problem: 977. Squares of a Sorted Array
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Approach: The solution avoids squaring each element and sorting the new array in order to find an O(n) solution using a different approach.


# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_abs = 1e4
        min_index = 0
        new_list = []

        for i in range(len(nums)):
            if abs(nums[i]) < min_abs:
                min_abs = abs(nums[i])
                min_index = i

        new_list.append(nums[min_index] ** 2)
        left = min_index - 1
        right = min_index + 1

        while left >= 0 or right < len(nums):
            if left >= 0 and right < len(nums):
                if abs(nums[left]) <= abs(nums[right]):
                    new_list.append(nums[left] ** 2)
                    left -= 1
                else:
                    new_list.append(nums[right] ** 2)
                    right += 1
            elif left < 0:
                new_list.append(nums[right] ** 2)
                right += 1
            else:
                new_list.append(nums[left] ** 2)
                left -= 1

        return new_list
