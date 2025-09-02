# Problem: 67. Add Binary
# Link: https://leetcode.com/problems/add-binary/

# Time Complexity: O(n)
# Space Complexity: O(n)
# (n = max(len(a), len(b) -  the maximum length of the two binary strings)


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length_a = len(a)
        length_b = len(b)
        i = length_a - 1
        j = length_b - 1
        carry = 0
        binary_sum = []

        while i >= 0 or j >= 0:  # O(n)

            if i >= 0 and j >= 0:
                current_sum = ((int(a[i]) + int(b[j])) % 2 + carry) % 2
                carry = (
                    (int(a[i]) & int(b[j])) | (int(a[i]) & carry) | (int(b[j]) & carry)
                )
                # use bitwise operators
            elif i >= 0:
                current_sum = (int(a[i]) + carry) % 2
                carry = int(a[i]) & carry
            elif j >= 0:
                current_sum = (int(b[j]) + carry) % 2
                carry = int(b[j]) & carry

            binary_sum.append(str(current_sum))
            i -= 1
            j -= 1

        if carry == 1:
            binary_sum.append(str(carry))
            # the list binary_sum can have n + 1 elements at most, in case of carry

        binary_sum.reverse()  # O(n)
        return "".join(binary_sum)  # O(n)
