# Problem: 27. Remove Element
# Link: https://leetcode.com/problems/remove-element/


# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        left = count = 0
        right = length - 1

        while left <= right:
            if nums[left] == val and nums[right] != val:
                aux = nums[left]
                nums[left] = nums[right]
                nums[right] = aux

            if nums[left] != val:
                left += 1

            if nums[right] == val:
                right -= 1
                count += 1

        return length - count
