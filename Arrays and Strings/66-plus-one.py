# Problem: 66. Plus One
# Link: https://leetcode.com/problems/plus-one/

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result_digits = []
        number = 0
        length = len(digits)

        for i in range(length):  # O(n)
            number = number * 10 + digits[i]

        number += 1  # O(1)

        # O(n)     (in the worst case, the number has n + 1 digits after adding to the original value)
        while number != 0:

            result_digits.append(number % 10)
            number /= 10

        result_digits.reverse()  # O(n)     (time complexity of the built-in function)
        return result_digits
