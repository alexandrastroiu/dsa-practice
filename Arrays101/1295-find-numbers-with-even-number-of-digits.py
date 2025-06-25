# Problem: 1295. Find Numbers with Even Numbers of Digits
# Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


# Time Complexity: O(n)


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_digits_num = 0

        for current_number in nums:
            digits = 0

            while current_number != 0:
                digits += 1
                current_number /= 10

            if digits % 2 == 0:
                even_digits_num += 1

        return even_digits_num
