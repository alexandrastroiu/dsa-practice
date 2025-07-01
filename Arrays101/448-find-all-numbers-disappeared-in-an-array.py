# Problem: 448. Find All Numbers Disappeared in an Array
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


# Time Complexity: O(n)
# Space Complexity: O(1) (assume the returned list does not count as extra space)


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0
        length = len(nums)
        missing_numbers = []

        while index < length:
            value = nums[index]
            if value != (index + 1):
                if nums[value - 1] != value:
                    aux = value
                    nums[index] = nums[value - 1]
                    nums[value - 1] = value
                else:
                    index += 1
            else:
                index += 1

        for i in range(length):
            if nums[i] != (i + 1):
                missing_numbers.append(i + 1)

        return missing_numbers
