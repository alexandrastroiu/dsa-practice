# Problem: 344. Reverse String
# Link: https://leetcode.com/problems/reverse-string/

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:  # use two-pointer technique
            aux = s[left]  # swap
            s[left] = s[right]
            s[right] = aux

            left += 1
            right -= 1  # O(1) extra space
