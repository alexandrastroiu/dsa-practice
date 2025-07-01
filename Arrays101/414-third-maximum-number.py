# Problem: 414. Third Maximum Number
# Link: https://leetcode.com/problems/third-maximum-number/


# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MIN_VALUE = (-2) ** 31 - 1
        max1 = MIN_VALUE
        max2 = MIN_VALUE
        max3 = MIN_VALUE

        for current_element in nums:
            if current_element > max1:
                max3 = max2
                max2 = max1
                max1 = current_element
            elif current_element > max2 and current_element != max1:
                max3 = max2
                max2 = current_element
            elif (
                current_element > max3
                and current_element != max2
                and current_element != max1
            ):
                max3 = current_element

        if max3 == MIN_VALUE:
            return max1
        else:
            return max3
