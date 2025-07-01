# Problem: 1299. Replace Elements with Greatest Element on Right Side
# Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/


# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_right = 0
        length = len(arr)

        for i in range(length - 1, -1, -1):
            value = arr[i]
            if i == length - 1:
                arr[i] = -1
            else:
                arr[i] = max_right
            if value > max_right:
                max_right = value

        return arr
