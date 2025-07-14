# Problem: 66. Plus One
# Link: https://leetcode.com/problems/plus-one/


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result_digits = []
        number = 0
        length = len(digits)

        for i in range(length):
            number = number * 10 + digits[i]

        number += 1

        while number != 0:
            result_digits.append(number % 10)
            number /= 10

        result_digits.reverse()
        return result_digits
