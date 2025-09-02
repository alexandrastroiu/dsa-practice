# Problem: 1089. Duplicate Zeros
# Link: https://leetcode.com/problems/duplicate-zeros/


# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0

        while i < length - 1:
            if arr[i] == 0:
                for j in range(length - 1, i, -1):
                    arr[j] = arr[j - 1]
                i += 2
            else:
                i += 1
